from lib.date_repositoty import DateRepository
from lib.date import Date
from datetime import datetime

"""
A global method to convert date-as-string input into datetime data
"""
def date_converter(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').date()

"""
When I call date repo #alldates 
I get a list of all dates from date tabla
"""

def test_all(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    assert repo.all()[:2] == [
        Date(1, date_converter('2023-10-24'), True, 3),
        Date(2, date_converter('2023-10-25'), True, 5)
    ]
    

"""
When calling #find with id
I get a specific date back
"""

def test_find(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    assert repo.find(1) ==  Date(1, date_converter('2023-10-24'), True, 3)

def test_filter_with_date(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    assert repo.filter_with_date('2023-10-24', True) == [
        Date(1, date_converter('2023-10-24'), True, 3)
    ]

# When filter with date is called and there is no availability nothing is returned
def test_find_with_unavailable_date(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    assert repo.filter_with_date('2023-10-28', True) == []

def test_filter_by_availability(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    assert repo.filter_by_property('available',True) == [
        Date(1, date_converter('2023-10-24'), True, 3),
        Date(2, date_converter('2023-10-25'), True, 5),
        Date(3, date_converter('2023-10-26'), True, 2),
        Date(4, date_converter('2023-10-27'), True, 3)
    ]

def test_create(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    date = Date(None, '2023-10-07', True, 4)

    repo.create(date)

    assert date.id == 11
    assert repo.all()[-2:] == [
        Date(10, date_converter('2023-10-03'), False, 2),
        Date(11, date_converter('2023-10-07'), True, 4)
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    repo.delete(10)

    assert repo.find(10) == "No item associated with id 10"

def test_delete_all_dates_for_space(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    repo.delete_by_space(3)

    assert repo.all() == [
        Date(2, date_converter('2023-10-25'), True, 5),
        Date(3, date_converter('2023-10-26'), True, 2),
        Date(5, date_converter('2023-10-28'), False, 5),
        Date(6, date_converter('2023-10-29'), False, 1),
        Date(7, date_converter('2023-10-30'), False, 1),
        Date(9, date_converter('2023-10-02'), False, 4),
        Date(10, date_converter('2023-10-03'), False, 2)
    ]

def test_updating_availability(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    repo.update_availability(1, False)

    assert repo.find(1) == Date(1, date_converter('2023-10-24'), False, 3)

