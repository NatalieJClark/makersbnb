from lib.user_repository import UserRepository
from lib.user import User
import hashlib

"""
When we call UserRepository#all
We get a list of all the User objects
"""
def test_list_all_users(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, 'name1@cmail.com', 'user1', '0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e'),
        User(2, 'name2@cmail.com', 'user2', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4'),
        User(3, 'name3@cmail.com', 'user3', '5906ac361a137e2d286465cd6588ebb5ac3f5ae955001100bc41577c3d751764')
    ]
    
"""
When we create a User object
It is reflected in the list when we call UserRepository#all
"""
def test_create_single_user(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    email = "Test Email"
    username = "Test Username"
    password = "Test Password"
    binary_test_password = (password).encode("utf-8")
    hashed_test_password = hashlib.sha256(binary_test_password).hexdigest()
    repository.create(email, username, password)
    # assert repository.create(email, password) == User(4, "Test email", hashed_test_password)
    assert repository.all() == [
        User(1, 'name1@cmail.com', 'user1', '0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e'),
        User(2, 'name2@cmail.com', 'user2', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4'),
        User(3, 'name3@cmail.com', 'user3', '5906ac361a137e2d286465cd6588ebb5ac3f5ae955001100bc41577c3d751764'),
        User(4, "Test Email", "Test Username", hashed_test_password)
    ]

def test_check_password_true(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    result = repository.check_password('name1@cmail.com', 'password1')
    assert result == True

def test_check_password_false(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    result = repository.check_password('name1@cmail.com', 'password9')
    assert result == False

def test_check_email_false(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    result = repository.check_password('user9', 'password1')
    assert result == False

"""
When we call UserRepository#find with an id
We get the User object for that id
"""
def test_find_user(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    assert repository.find(2) == User(2, 'name2@cmail.com', 'user2', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4')

"""
When we call UserRepository#update with a user object
It is reflected in the list when we call UserRepository#all
"""
def test_update_user(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    user = repository.find(1)
    user.email = "new@email1"
    user.password = "124A!12346"
    assert repository.update(user) == None
    assert repository.all() == [
        User(1, 'new@email1', 'user1', 'ca97cf06eabb3000ecbc4f7b6966924838b14395d03d9bd4cd69725e65438498'),
        User(2, 'name2@cmail.com', 'user2', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4'),
        User(3, 'name3@cmail.com', 'user3', '5906ac361a137e2d286465cd6588ebb5ac3f5ae955001100bc41577c3d751764'),
    ]

"""
When we call UserRepository#delete with an id
That User object is no longer in the list when we call UserRepository#all
"""
def test_delete_user(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    assert repository.delete(3) == None
    assert repository.all() == [
        User(1, 'name1@cmail.com', 'user1', '0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e'),
        User(2, 'name2@cmail.com', 'user2', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4')
    ]

def test_filter_by_username(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    result = repository.filter_by_property('username', 'user2')
    assert result == [User(2, 'name2@cmail.com', 'user2', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4')]

def test_filter_by_id(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    result = repository.filter_by_property('id', 2)
    assert result == [User(2, 'name2@cmail.com', 'user2', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4')]

def test_filter_by_email(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    result = repository.filter_by_property('email', 'name2@cmail.com')
    assert result == [User(2, 'name2@cmail.com', 'user2', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4')]