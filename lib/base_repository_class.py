class BaseModelManager:

    """
    Base Repository motel with all CRUD methods.
    Implement create method on child models.
    """

    def __init__(self, connection) -> None:
        self._connection = connection
        self._model_class = None
        self._table_name = None

    def all(self):
        query = "SELECT * FROM %s;" % self._table_name
        rows = self._connection.execute(query)
        return [self._model_class(**row) for row in rows]

    def find(self, object_id):
        query = "SELECT * FROM %s WHERE id = %s;" % (self._table_name, object_id)
        row = self._connection.execute(query)[0]
        return self._model_class(**row)

    def delete(self, object_id):
        query = "DELETE FROM %s WHERE id=%s;" % (self._table_name, object_id)
        self._connection.execute(query)
        return None

    def filter_by_property(self, property, value):        
        """
        A method to return all objects filtered by a property
        where property is a column name, and value is the specific filtering parameter
        """
        query = 'SELECT * FROM %s WHERE %s = %s;' % (self._table_name, property, value)
        rows = self._connection.execute(query)
        print(rows)
        return [self._model_class(**row) for row in rows]

    def create(self):
        raise NotImplementedError
