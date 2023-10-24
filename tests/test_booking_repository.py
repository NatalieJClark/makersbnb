from lib.booking_repository import BookingRepository
from lib.booking import Booking

"""
When we call Bookingepository#all
we get a list of all booking objects
"""
def test_get_all_bookings(db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')
    repository = BookingRepository(db_connection)
    assert repository.all() == [
        Booking(1, True, 5, 5, 1, 3),
        Booking(2, False, 3, 1, 3, 2)
        ]

"""
When we create a Booking object
It is reflected in the list when we call BookingRepository#all
"""
def test_create_single_booking(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = BookingRepository(db_connection)
    booking = Booking(None, False, 1, 2, 3, 1)
    assert repository.create(booking) == None
    assert repository.all() == [
        Booking(1, True, 5, 5, 1, 3),
        Booking(2, False, 3, 1, 3, 2),
        Booking(3, False, 1, 2, 3, 1)
        ]


"""
When we call BookingRepository#find with an id
We get the Booking object for that id
"""
def test_find_booking(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = BookingRepository(db_connection)
    assert repository.find(2) == Booking(2, False, 3, 1, 3, 2)

"""
When we call BookingRepository#update with a booking object
It is reflected in the list when we call BookingRepository#all
"""
def test_update_booking(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = BookingRepository(db_connection)
    booking = repository.find(1)
    booking.confirmed = False
    booking.space_id = 1
    booking.date_id = 1
    booking.guest_id = 1
    booking.owner_id = 1
    assert repository.update(booking) == None
    print(repository.all())
    assert repository.all() == [
        Booking(1, False, 1, 1, 1, 1),
        Booking(2, False, 3, 1, 3, 2)
        ]

"""
When we call BookingRepository#delete with an id
That Booking object is no longer in the list when we call BookingRepository#all
"""
def test_delete_user(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = BookingRepository(db_connection)
    assert repository.delete(2) == None
    assert repository.all() == [
        Booking(1, True, 5, 5, 1, 3)
        ]

