from lib.booking_request import BookingRequest

"""
When we construct a booking_request object
We can get all the properties back
"""
def test_construct_booking_request():
    booking_request = BookingRequest(1, True, 1, 2, 3, 4)
    assert booking_request.id == 1
    assert booking_request.confirmed == True
    assert booking_request.space_id == 1
    assert booking_request.date_id == 2
    assert booking_request.guest_id == 3
    assert booking_request.owner_id == 4

"""
When we have two identical booking_request objects
They are considered equal
"""
def test_booking_request_eq():
    booking_request_1 = BookingRequest(1, True, 1, 2, 3, 4)
    booking_request_2 = BookingRequest(1, True, 1, 2, 3, 4)
    assert booking_request_1 == booking_request_2

"""
BookingRequest objects format to string nicely
"""
def test_booking_request_formats_to_string():
    booking_request = BookingRequest(1, True, 1, 2, 3, 4)
    assert str(booking_request) == "Booking Request(1, True, 1, 2, 3, 4)"
