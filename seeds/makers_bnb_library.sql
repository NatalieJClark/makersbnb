DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS dates CASCADE;
DROP SEQUENCE IF EXISTS dates_id_seq;
DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email text,
    username text,
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

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    confirmed boolean,
    space_id int,
    date_id int,
    guest_id int,
    owner_id int,
    constraint fk_spaces_bookings foreign key(space_id)
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

INSERT INTO users (email, username, password) VALUES ('name1@cmail.com', 'name1', 'password1');
INSERT INTO users (email, username, password) VALUES ('name2@cmail.com', 'name2', 'password2');
INSERT INTO users (email, username, password) VALUES ('name3@cmail.com', 'name3', 'password3');

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

INSERT INTO bookings (confirmed, space_id, date_id, guest_id, owner_id) VALUES (True, 5, 5, 1, 3);
INSERT INTO bookings (confirmed, space_id, date_id, guest_id, owner_id) VALUES (False, 3, 1, 3, 2);
