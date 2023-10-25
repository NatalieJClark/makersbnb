from datetime import datetime
from lib.base_repository_class import BaseModelManager
from lib.date import Date

class DateRepository(BaseModelManager):
    def __init__(self, connection) -> None:
        super().__init__(connection)
        self._model_class = Date
        self._table_name = 'dates'

    def filter_with_date(self, date, available):
        """
        to find available spaces on a specific date, give date and True.
        to find unavailable dates on a specific date, give date and False.
        """
        rows = self._connection.execute(
            "SELECT * FROM dates WHERE date = %s AND available = %s", [date, available]
        )
        return [self._model_class(**row) for row in rows]
    
    def create(self, date):
        """ to add a new available date, enter the date with 'available' set to True and the space's id """
        rows = self._connection.execute(
            "INSERT INTO dates (date, available, space_id) VALUES (%s, %s, %s) RETURNING id",
            [date.date, date.available, date.space_id]
        )
        row = rows[0]
        date.id = row['id']
        return None
    
    def delete_by_space(self, space_id):
        """ to delete all dates associated with a space, enter the space id """
        self._connection.execute(
            "DELETE FROM dates WHERE space_id = %s", [space_id]
        )
        return None
    
        
    def update_availability(self, date_id, new_available):
        """
        To update a date's availability to available, give the date_id and True.
        To update a date's availability to unavailable, give the date_id and False.
        """
        self._connection.execute(
            "UPDATE dates SET available = %s WHERE id = %s", 
            [new_available, date_id]
        )
        return None

