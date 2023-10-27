import os
from flask import Flask, request, render_template, session, redirect, url_for, flash
import hashlib
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.space_repo import SpaceRepository
from lib.space import Space
from lib.date_repositoty import DateRepository
from lib.booking_request import BookingRequest
from lib.booking_request_repository import BookingRequestRepository

from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")


# Routes

@app.route('/index', methods=['GET'])
def get_login():
    return render_template('/index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('get_login'))

@app.route('/users/new', methods=['GET'])
def get_new_user():
    return render_template('/users/new.html')

@app.route('/spaces/list')
def space_list():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    logged = check_login_status()
    spaces = repo.all()
    return render_template('/spaces/list.html', spaces=spaces, logged=logged)

@app.route('/spaces/detail/<id>', methods=['GET', 'POST'])
def space_detail(id):
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    space = space_repository.find(id)
    date_repository = DateRepository(connection)
    dates = date_repository.filter_by_property('space_id', space.id)

    if request.method == 'POST':
        booking_request_repository = BookingRequestRepository(connection)
        date_id = request.form.get('date')
        user_id = session.get('user_id')
        booking_request = BookingRequest(
            None, 
            None, 
            space_id=space.id, 
            date_id=date_id, 
            guest_id=user_id, 
            owner_id=space.user_id
            )
        booking_request_repository.create(booking_request)
        flash("Your booking has been created. You will receive the confirmation once it is confirmed :)")
    return render_template('/spaces/detail.html', space=space, dates=dates)
    logged = check_login_status()
    return render_template('/spaces/detail.html', space=space, dates=dates, logged=logged)

@app.route('/users/<int:id>/spaces')
def space_list_by_user(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.filter_by_property("user_id", id)
    logged = check_login_status()
    return render_template('/spaces/list.html', spaces=spaces, logged=logged)

@app.route('/index', methods=['POST'])
def login():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    email = request.form['email']
    password = request.form['password']
    if repo.check_password(email, password):
        rows = repo.filter_by_property('email', email)
        user = rows[0]
        # set user id
        session['user_id'] = user.id
        
        return redirect(url_for('space_list'))
    else:
        error = "*Email and Password don't match. Please try again."
        return render_template('/index.html', errors=error), 400
    
@app.route('/users/new', methods=['POST'])
def user_create():
    connection = get_flask_database_connection(app)

    email = request.form['email']
    username = request.form['username']
    password = request.form['password1']
    confirm_password = request.form['password2']

    if password == confirm_password:
        user = UserRepository(connection)
        user.create(email, username, password)
        print(user)
        print(UserRepository(connection).all())
    else:
        error = "*Your passwords don't match. Please try again."
        return render_template("users/new.html", errors=error), 400
    
    return redirect(url_for('get_login'))

@app.route('/spaces/new', methods=['GET', 'POST'])
def space_create():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    logged = check_login_status()
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        size = request.form.get('size')
        location = request.form.get('location')
        price = request.form.get('price')
        owner_id = session.get('user_id')
        space = Space(None, name, description, size, location, price, owner_id)
        repo.create(space)

        return redirect(url_for('space_list_by_user', id=owner_id, logged=logged))
    else:

        return render_template('account.html')
    
@app.route('/user/requests', methods = ['GET', 'POST'])
def request_list():
    connection = get_flask_database_connection(app)
    booking_request_repo = BookingRequestRepository(connection)
    owner_id = session.get('user_id')
    bookings = booking_request_repo.find_request_details('owners.id', owner_id)
    if request.method == 'POST':
        booking_id = request.form.get('booking_id')
        booking = booking_request_repo.find(booking_id)
        booking.confirmed = True
        booking_request_repo.update(booking)
        flash("Booking has been confirmed.")
        return redirect(url_for('request_list'))
    return render_template('/bookings/list.html', bookings=bookings)

@app.route('/user/mybookings', methods = ['GET', 'POST'])
def my_bookings_list():
    connection = get_flask_database_connection(app)
    booking_request_repo = BookingRequestRepository(connection)
    guest_id = session.get('user_id')
    bookings = booking_request_repo.find_request_details('guests.id', guest_id)
    return render_template('/bookings/booking_list.html', bookings=bookings)
        return render_template('/spaces/new.html', logged=logged)

def check_login_status():
    # global method to check if user is logged in
    if 'user_id' not in session:
        return False
    return True


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))