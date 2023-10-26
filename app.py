import os
import hashlib
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.space_repo import SpaceRepository
from lib.space import Space
from dotenv import load_dotenv
from lib.date_repositoty import DateRepository

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

@app.route('/spaces/detail/<id>')
def space_detail(id):
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    space = space_repository.find(id)
    date_repository = DateRepository(connection)
    dates = date_repository.filter_by_property('space_id', space.id)

    return render_template('/spaces/detail.html', space=space, dates=dates)

@app.route('/users/<int:id>/spaces')
def space_list_by_user(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.filter_by_property("user_id", id)
    return render_template('/spaces/list.html', spaces=spaces)

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
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        size = request.form.get('size')
        location = request.form.get('location')
        price = request.form.get('price')
        owner_id = session.get('user_id')
        space = Space(None, name, description, size, location, price, owner_id)
        repo.create(space)

        return redirect(url_for('space_list_by_user', id=owner_id))
    else:
        return render_template('/spaces/new.html')



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