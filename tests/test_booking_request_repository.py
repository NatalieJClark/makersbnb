from lib.booking_request_repository import  BookingRequestRepository
from lib.booking_request import  BookingRequest
import datetime

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
    booking_request = BookingRequest(None, None, 1, 2, 3, 1)
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
Calling BookingRequestRepository#find_request
With a guest id
Gets details of a BookingRequest as a dictionary
"""
def test_find_request_details_by_guest_id(db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')
    repository = BookingRequestRepository(db_connection)
    result = repository.find_request_details('guests.id', 1)
    assert result == [{
        'id': 1,
        'space_name': 'myplace5',
        'date': datetime.date(2023, 10, 28), 
        'available': False, 'confirmed': True, 
        'owners_username': 'user3', 
        'owners_email': 'name3@cmail.com', 
        'guests_username': 'user1', 
        'guests_email': 'name1@cmail.com'
    }]

"""
Calling BookingRequestRepository#find_request
With a owner id
Gets details of a BookingRequest as a dictionary
"""
def test_find_request_details_by_owner_id(db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')
    repository = BookingRequestRepository(db_connection)
    result = repository.find_request_details('owners.id', 2)
    assert result == [{
        'id': 2,
        'space_name': 'myplace3',
        'date': datetime.date(2023, 10, 24), 
        'available': True, 'confirmed': False, 
        'owners_username': 'user2', 
        'owners_email': 'name2@cmail.com', 
        'guests_username': 'user3', 
        'guests_email': 'name3@cmail.com'
    }]

def test_find_request_details_by_guest_username(db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')
    repository = BookingRequestRepository(db_connection)
    result = repository.find_request_details('guests.username', 'user1')
    assert result == [{
        'id': 1,
        'space_name': 'myplace5',
        'date': datetime.date(2023, 10, 28), 
        'available': False, 'confirmed': True, 
        'owners_username': 'user3', 
        'owners_email': 'name3@cmail.com', 
        'guests_username': 'user1', 
        'guests_email': 'name1@cmail.com'
    }]