import os
from flask import Flask, request, render_template, session, redirect
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    if UserRepository.check_password(username, password):
        user = UserRepository.filter_by_property('username', username)
        # set user id
        session['user_id'] = user.id

        return render_template('home_page.html')
    else:
        return render_template('login_error.html')

# only if a user is signed-in
# this route can be re used for any pages that are only available
# if the user is logged in
@app.route('/account_page') #can change page
def account_page():
    if 'user_id' not in session:
        return redirect('/index')
    else:
        return render_template('account.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
