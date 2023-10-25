from lib.user import User


"""
When we construct a user with an email, username and password
We can get those properties back
"""
def test_user_constructs():
    user = User(1, "Test email", "Test User", "Test Password")
    assert user.id == 1
    assert user.email == "Test email"
    assert user.username == "Test User"
    assert user.password == "Test Password"

"""
When we have two identical User objects
They are considered equal
"""
def test_identical_user_objects_equat():
    user_1 = User(1, "Test email", "Test User", "Test Password")
    user_2 = User(1, "Test email", "Test User", "Test Password")
    assert user_1 == user_2

"""
When we format a user 
We will get a string
"""
def test_user_formats_to_string():
    user = User(1, "Test Email", "Test User", "Test Password")
    assert str(user) == "1, Test Email, Test User, Test Password"