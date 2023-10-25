from lib.user import User
from lib.base_repository_class import BaseModelManager
import hashlib


class UserRepository(BaseModelManager):
    def __init__(self, connection) -> None:
        super().__init__(connection)
        self._model_class = User
        self._table_name = 'users'

    def create(self, email, password):
        #hash the password
        binary_password = password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()

        rows = self._connection.execute(
            'INSERT INTO users (email, password) VALUES (%s, %s) RETURNING id',
            [email, hashed_password]
        )
        # user.id = rows[0].get('id')
        # return user

    def check_password(self, email, password_attempt):
        # hash the password attempt
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        # Check whether there is a user in the database with the given email
        # and a matching password hash, using a SELECT statement.
        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s',
            [email, hashed_password_attempt]
        )

        # If that SELECT finds any rows, the password is correct.
        return len(rows) > 0

    #TODO: Move it to BASE CLASS
    def update(self, user):
        self._connection.execute(
            'UPDATE users SET email = %s, username = %s, password = %s WHERE id = %s',
            [user.email, user.username, user.password, user.id])
        
        return None
    
