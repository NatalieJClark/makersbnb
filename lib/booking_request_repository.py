from lib.base_repository_class import BaseModelManager
from lib.booking_request import BookingRequest

class BookingRequestRepository(BaseModelManager):
    def __init__(self, connection) -> None:
        super().__init__(connection)
        self._model_class = BookingRequest
        self._table_name = "booking_requests"

    def create(self, booking_request):
        self._connection.execute('INSERT INTO booking_requests (confirmed, space_id, date_id, guest_id, owner_id) VALUES (%s, %s, %s, %s, %s)',
        [False, booking_request.space_id, booking_request.date_id, booking_request.guest_id, booking_request.owner_id])
        return None


    def update(self, booking_request):
        self._connection.execute(
            'UPDATE booking_requests SET confirmed = %s, space_id = %s, date_id = %s, guest_id = %s, owner_id = %s WHERE id = %s',
            [booking_request.confirmed, booking_request.space_id, booking_request.date_id, booking_request.guest_id, booking_request.owner_id, booking_request.id])
        return None
    
    def deny_request(self, booking_request):
        self._connection.execute(
            'UPDATE booking_requests SET confirmed = %s WHERE id = %s',
            [False, booking_request.id])
        return None

    # def confirm_request

    # def find_request