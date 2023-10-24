from lib.space import Space
from lib.space_repo import SpaceRepository


def test_find_by_id(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    space_repo = SpaceRepository(db_connection)
    assert space_repo.find(1) == Space(
        1, "myplace1", "1 this is a description", 40, "E10 9BY", 10.0, 1
    )


def test_all_spaces(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    space_repo = SpaceRepository(db_connection)
    assert space_repo.all()[:2] == [
        Space(1, "myplace1", "1 this is a description", 40, "E10 9BY", 10.0, 1),
        Space(2, "myplace2", "2 this is a description", 50, "N1 9UY", 15.0, 1),
    ]

def test_create_space(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    space_repo = SpaceRepository(db_connection)
    new_space = Space(
        None, "myplace_new", "1 this is a description new", 40, "E10 9BY", 10.0, 1
    )
    space_repo.create(new_space)
    assert space_repo.all()[-1:] == [
        Space(
        6, "myplace_new", "1 this is a description new", 40, "E10 9BY", 10.0, 1
    )
    ]

def test_delete_space(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    space_repo = SpaceRepository(db_connection)
    space_repo.delete(1)
    assert space_repo.all()[:2] == [
        Space(2, "myplace2", "2 this is a description", 50, "N1 9UY", 15.0, 1),
        Space(3, "myplace3", "3 this is a description", 60, 'E1 5BY', 20.0, 2),
    ]

def test_all_spaces_by_user_id(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    space_repo = SpaceRepository(db_connection)
    assert space_repo.filter_by_property('user_id',3) == [
        Space(4, 'myplace4', '4 this is a description', 74, 'SW10 9BJ', 30.0, 3),
        Space(5, 'myplace5', '5 this is a description', 67, 'E14 9TY', 18.0, 3)
    ]
