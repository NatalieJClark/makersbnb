import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repo import SpaceRepository
from lib.space import Space


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


@app.route('/users/<int:id>/spaces')
def space_list_by_user(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.filter_by_property("user_id", id)
    return render_template('/spaces/list.html', spaces=spaces)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
