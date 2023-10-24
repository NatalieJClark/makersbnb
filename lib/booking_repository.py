from lib.base_repository_class import BaseModelManager
from lib.booking import Booking

class BookingRepository(BaseModelManager):
    def __init__(self, connection) -> None:
        super().__init__(connection)
        self._model_class = Booking
        self._table_name = "bookings"

    def create(self, booking):
        self._connection.execute('INSERT INTO bookings (confirmed, space_id, date_id, guest_id, owner_id) VALUES (%s, %s, %s, %s, %s)',
        [booking.confirmed, booking.space_id, booking.date_id, booking.guest_id, booking.owner_id])
        return None


    def update(self, booking_id):
        pass