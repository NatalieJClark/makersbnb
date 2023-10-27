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

INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('Seaside Villa', 'A luxurious villa by the beach', 150, 'Malibu', 200.0, 1);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('Mountain Retreat', 'Cozy cabin with mountain views', 60, 'Aspen', 120.0, 1);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('Downtown Loft', 'Modern loft in the heart of the city', 70, 'New York', 180.0, 1);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('Country Cottage', 'Charming cottage in the countryside', 80, 'Cotswolds', 90.0, 1);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('Beach House', 'Relaxing beachfront house', 120, 'Miami', 250.0, 1);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('Ski Chalet', 'Ski-in/ski-out chalet', 100, 'Whistler', 220.0, 1);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('Rural Farmhouse', 'Rustic farmhouse in the countryside', 110, 'Tuscany', 110.0, 1);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('City View Apartment', 'Apartment with city skyline view', 50, 'Chicago', 150.0, 1);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('Desert Oasis', 'Luxury desert oasis', 90, 'Scottsdale', 190.0, 1);
INSERT INTO spaces (name, description, size, location, price, user_id) VALUES ('Historic Mansion', 'Elegant historic mansion', 200, 'Charleston', 280.0, 1);

-- Insert 20 available dates for the 10 spaces

INSERT INTO dates (date, available, space_id) VALUES ('2023-11-10', True, 1);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-11', True, 1);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-12', True, 1);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-13', True, 1);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-14', True, 2);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-15', True, 3);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-16', True, 3);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-17', True, 3);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-18', True, 4);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-19', True, 5);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-20', True, 5);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-21', True, 6);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-22', True, 7);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-23', True, 7);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-24', True, 8);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-25', True, 8);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-26', True, 8);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-27', True, 9);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-28', True, 9);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-29', True, 10);
INSERT INTO dates (date, available, space_id) VALUES ('2023-11-30', True, 10);