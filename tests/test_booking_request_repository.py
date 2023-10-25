from lib.booking_request_repository import  BookingRequestRepository
from lib.booking_request import  BookingRequest

"""
When we call BookingRequestRepository#all
we get a list of all BookingRequest objects
"""
def test_get_all_booking_requests(db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')
    repository = BookingRequestRepository(db_connection)
    assert repository.all() == [
        BookingRequest(1, True, 5, 5, 1, 3),
        BookingRequest(2, False, 3, 1, 3, 2)
        ]

"""
When we create a BookingRequest object
It creates a not corfirmed Booking object
Which is reflected in the list when we call BookingRequestRepository#all
"""
def test_create_single_booking_request(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = BookingRequestRepository(db_connection)
    booking_request = BookingRequest(None, False, 1, 2, 3, 1)
    assert repository.create(booking_request) == None
    assert repository.all() == [
        BookingRequest(1, True, 5, 5, 1, 3),
        BookingRequest(2, False, 3, 1, 3, 2),
        BookingRequest(3, False, 1, 2, 3, 1)
        ]


"""
When we call BookingRequestRepository#find with an id
We get the booking_request object for that id
"""
def test_find_booking_request(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = BookingRequestRepository(db_connection)
    assert repository.find(2) == BookingRequest(2, False, 3, 1, 3, 2)

"""
When we call BookingRequestRepository#update with a BookingRequest object
It is reflected in the list when we call BookingRequestRepository#all
"""
def test_update_booking_request(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = BookingRequestRepository(db_connection)
    booking_request = repository.find(1)
    booking_request.confirmed = False
    booking_request.space_id = 1
    booking_request.date_id = 1
    booking_request.guest_id = 1
    booking_request.owner_id = 1
    assert repository.update(booking_request) == None
    print(repository.all())
    assert repository.all() == [
        BookingRequest(1, False, 1, 1, 1, 1),
        BookingRequest(2, False, 3, 1, 3, 2)
        ]

"""
When we call BookingRequestRepository#delete with an id
That BookingRequest object is no longer in the list when we call BookingRequestRepository#all
"""
def test_delete_booking_request(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = BookingRequestRepository(db_connection)
    assert repository.delete(2) == None
    assert repository.all() == [
        BookingRequest(1, True, 5, 5, 1, 3)
        ]
    
"""
When we call BookingRequestRepository#deny_request
The BookingRequest object confirmed property is updated to False
And this is reflected in the list of BookingRequest objects when we call #all
"""
def test_deny_request(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = BookingRequestRepository(db_connection)
    booking_request = repository.find(1)
    assert repository.deny_request(booking_request) ==  None
    assert repository.all() == [
        BookingRequest(1, False, 5, 5, 1, 3),
        BookingRequest(2, False, 3, 1, 3, 2)
        ]

