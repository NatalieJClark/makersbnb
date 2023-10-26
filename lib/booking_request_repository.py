from lib.base_repository_class import BaseModelManager
from lib.booking_request import BookingRequest

class BookingRequestRepository(BaseModelManager):
    def __init__(self, connection) -> None:
        super().__init__(connection)
        self._model_class = BookingRequest
        self._table_name = "booking_requests"

    def create(self, booking_request):
        self._connection.execute('INSERT INTO booking_requests (space_id, date_id, guest_id, owner_id) VALUES (%s, %s, %s, %s)',
        [booking_request.space_id, booking_request.date_id, booking_request.guest_id, booking_request.owner_id])
        return None


    def update(self, booking_request):
        self._connection.execute(
            'UPDATE booking_requests SET confirmed = %s, space_id = %s, date_id = %s, guest_id = %s, owner_id = %s WHERE id = %s',
            [booking_request.confirmed, booking_request.space_id, booking_request.date_id, booking_request.guest_id, booking_request.owner_id, booking_request.id])
        return None

    # Returns booking request details as a list of dictionaries
    # Keys:
    #       space_name, date, available, confirmed
    #       owners_username, owners_email, 
    #       guest_username, guests_email
    def find_request_details(self, property, value):
        query = """
        SELECT booking_requests.id,
                spaces.name AS space_name, 
                dates.date, dates.available,
                booking_requests.confirmed,
                owners.username AS owners_username,
                owners.email AS owners_email,
                guests.username AS guests_username,
                guests.email AS guests_email
        FROM booking_requests
            JOIN spaces ON booking_requests.space_id = spaces.id
            JOIN dates ON booking_requests.date_id = dates.id
            JOIN users AS owners ON booking_requests.owner_id = owners.id
            JOIN users AS guests ON booking_requests.guest_id = guests.id
        WHERE {} = %s;
        """.format(property)
        rows = self._connection.execute(query, (value,))
        return [row for row in rows]