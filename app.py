import os
from flask import Flask, request, render_template, session, redirect, sessions
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.space_repo import SpaceRepository
from lib.space import Space
from lib.date_repositoty import DateRepository
from lib.booking_request import BookingRequest
from lib.booking_request_repository import BookingRequestRepository


app = Flask(__name__)

# Routes

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('/index.html')

@app.route('/users/new', methods=['GET'])
def get_new_user():
    return render_template('/users/create.html')

@app.route('/spaces/list')
def space_list():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.all()
    return render_template('/spaces/list.html', spaces=spaces)

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
        
    return render_template('/spaces/detail.html', space=space, dates=dates)

@app.route('/users/<int:id>/spaces')
def space_list_by_user(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.filter_by_property("user_id", id)
    return render_template('/spaces/list.html', spaces=spaces)

@app.route('/index', methods=['POST'])
def login_post():
    connection = get_flask_database_connection(app)
    username = request.form['username']
    password = request.form['password']

    if UserRepository(connection).check_password(username, password):
        user = UserRepository(connection).filter_by_property('username', username)
        # set user id
        session['user_id'] = user.id

        return render_template('home_page.html')
    else:
        return render_template('login_error.html')
    
@app.route('/sign-up', methods=['POST'])
def sign_up_post():
    connection = get_flask_database_connection(app)

    email = request.form('email')
    username = request.form['username']
    password = request.form['password1']
    confirm_password = request.form['password2']

    if password == confirm_password:
        user = UserRepository(connection)
        user.create(email, username, password)

# only if a user is signed-in
# this route can be re used for any pages that are only available
# if the user is logged in
@app.route('/account_page') #can change page
def account_page():
    if 'user_id' not in session:
        return redirect('/sign-up')
    else:
        return render_template('account.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))