import os
from datetime import datetime, timedelta
from flask import Flask, request, render_template, session, redirect, url_for, flash
import hashlib
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.space_repo import SpaceRepository
from lib.space import Space
from lib.date_repositoty import DateRepository
from lib.booking_request import BookingRequest
from lib.booking_request_repository import BookingRequestRepository
from lib.date import Date
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")


# Routes

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('/login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('get_login'))

@app.route('/users/new', methods=['GET'])
def get_new_user():
    return render_template('/users/new.html')

@app.route('/home')
# @app.route('/spaces/list')
def space_list():
    username = get_username()
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    logged = check_login_status()
    spaces = repo.all()
    return render_template('/spaces/list.html', spaces=spaces, logged=logged, username=username)

@app.route('/spaces/detail/<id>', methods=['GET', 'POST'])
def space_detail(id):
    logged = check_login_status()
    if not logged:
        return redirect(url_for('get_login'))
    username = get_username()
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
        
    return render_template('/spaces/detail.html', space=space, dates=dates, logged=logged, username=username)
    

@app.route('/users/<int:id>/spaces')
def space_list_by_user(id):
    logged = check_login_status()
    if not logged:
        return redirect(url_for('get_login'))
    username = get_username()
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.filter_by_property("user_id", id)
    return render_template('/spaces/list.html', spaces=spaces, logged=logged, username=username)

@app.route('/login', methods=['POST'])
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
        session['username'] = user.username
        
        return redirect(url_for('space_list'))
    else:
        error = "*Email and Password don't match. Please try again."
        return render_template('/login.html', errors=error), 400
    
@app.route('/sign-in')
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
    logged = check_login_status()
    if not logged:
        return redirect(url_for('get_login'))
    username = get_username()
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    if request.method == 'POST':

        dates = []
        delta = timedelta(days=1)
        start_date = datetime.fromisoformat(request.form.get('date1')).date()

        end_date = datetime.fromisoformat(request.form.get('date2')).date()
        while start_date <= end_date:
            dates.append(start_date.isoformat())
            start_date += delta

        date_repository = DateRepository(connection)

        name = request.form.get('name')
        description = request.form.get('description')
        size = request.form.get('size')
        location = request.form.get('location')
        price = request.form.get('price')
        owner_id = session.get('user_id')
        space = Space(None, name, description, size, location, price, owner_id)
        new_space = repo.create(space)
        for date in dates:
            new_date = Date(None, date, True, new_space.id)
            date_repository.create(new_date)

        flash('Your space has been created.')
        return redirect(url_for('space_list_by_user', id=owner_id, logged=logged, username=username))
    else:

        return render_template('spaces/new.html', logged=logged, username=username)
    
@app.route('/user/requests', methods = ['GET', 'POST'])
def request_list():
    logged = check_login_status()
    if not logged:
        return redirect(url_for('get_login'))
    username = get_username()
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
    return render_template('/bookings/list.html', bookings=bookings, logged=logged, username=username)

@app.route('/user/mybookings', methods = ['GET', 'POST'])
def my_bookings_list():
    logged = check_login_status()
    if not logged:
        return redirect(url_for('get_login'))
    username = get_username()
    connection = get_flask_database_connection(app)
    booking_request_repo = BookingRequestRepository(connection)
    guest_id = session.get('user_id')
    bookings = booking_request_repo.find_request_details('guests.id', guest_id)
    return render_template('/bookings/booking_list.html', bookings=bookings, logged=logged, username=username)


def check_login_status():
    # global method to check if user is logged in
    if 'user_id' not in session:
        return False
    return True

def get_username():
    if 'user_id' in session:
        return session.get('username')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))