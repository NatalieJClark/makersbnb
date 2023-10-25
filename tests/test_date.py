from lib.date import Date

"""
When Constructing Date object
It is reflected on the properties
"""

def test_construct():
    date = Date(1, '2023-10-24', True, 4)

    assert date.id == 1
    assert date.date == '2023-10-24'
    assert date.available == True
    assert date.space_id == 4

def test_eq():
    date1 = Date(1, '2023-10-24', True, 4)
    date2 = Date(1, '2023-10-24', True, 4)

    assert date1 == date2

def test_format():
    date = Date(1, '2023-10-24', True, 4)

    assert str(date) == "Date(1, 2023-10-24, True, 4)"