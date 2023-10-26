DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS dates CASCADE;
DROP SEQUENCE IF EXISTS dates_id_seq;
DROP TABLE IF EXISTS booking_requests CASCADE;
DROP SEQUENCE IF EXISTS booking_requests_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text,
    password text
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    size int,
    location text,
    price float,
    user_id int,
    constraint fk_users foreign key(user_id)
    references users(id)
    on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS dates_id_seq;
CREATE TABLE dates (
    id SERIAL PRIMARY KEY,
    date date,
    available boolean,
    space_id int,
    constraint fk_spaces foreign key(space_id)
    references spaces(id)
    on delete cascade
);
CREATE INDEX idx_space_id ON dates (space_id);

CREATE SEQUENCE IF NOT EXISTS booking_requests_id_seq;
CREATE TABLE booking_requests (
    id SERIAL PRIMARY KEY,
    confirmed boolean DEFAULT False,
    space_id int,
    date_id int,
    guest_id int,
    owner_id int,
    constraint fk_spaces_booking_requests foreign key(space_id)
    references spaces(id)
    on delete cascade,
    constraint fk_dates foreign key(date_id)
    references dates(id)
    on delete cascade,
    constraint fk_guests foreign key(guest_id)
    references users(id)
    on delete cascade,
    constraint fk_owners foreign key(owner_id)
    references users(id)
    on delete cascade
);

INSERT INTO users (email, username, password) VALUES ('name1@cmail.com', 'user1', '0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e');
INSERT INTO users (email, username, password) VALUES ('name2@cmail.com', 'user2','6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4');
INSERT INTO users (email, username, password) VALUES ('name3@cmail.com', 'user3','5906ac361a137e2d286465cd6588ebb5ac3f5ae955001100bc41577c3d751764');

INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('myplace1', '1 this is a description', 40, 'E10 9BY', 10.0, 1);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('myplace2', '2 this is a description', 50, 'N1 9UY', 15.0, 1);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('myplace3', '3 this is a description', 60, 'E1 5BY', 20.0, 2);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('myplace4', '4 this is a description', 74, 'SW10 9BJ', 30.0, 3);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('myplace5', '5 this is a description', 67, 'E14 9TY', 18.0, 3);

INSERT INTO dates (date, available, space_id) VALUES ('2023-10-24', True, 3);
INSERT INTO dates (date, available, space_id) VALUES ('2023-10-25', True, 5);
INSERT INTO dates (date, available, space_id) VALUES ('2023-10-26', True, 2);
INSERT INTO dates (date, available, space_id) VALUES ('2023-10-27', True, 3);
INSERT INTO dates (date, available, space_id) VALUES ('2023-10-28', False, 5);
INSERT INTO dates (date, available, space_id) VALUES ('2023-10-29', False, 1);
INSERT INTO dates (date, available, space_id) VALUES ('2023-10-30', False, 1);
INSERT INTO dates (date, available, space_id) VALUES ('2023-10-01', False, 3);
INSERT INTO dates (date, available, space_id) VALUES ('2023-10-02', False, 4);
INSERT INTO dates (date, available, space_id) VALUES ('2023-10-03', False, 2);

INSERT INTO booking_requests (confirmed, space_id, date_id, guest_id, owner_id) VALUES (True, 5, 5, 1, 3);
INSERT INTO booking_requests (confirmed, space_id, date_id, guest_id, owner_id) VALUES (False, 3, 1, 3, 2);
