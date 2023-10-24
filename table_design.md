## One to Many Tables Design Recipe Template

*Copy this recipe template to design and create two related database tables from a specification.*

## 1. Extract nouns from the user stories or specification

```markdown
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a user
So that I can manage my account
I want to be able to sign up and log in with email, username and password

(create db, map db)

As a user
So that I can list all my spaces to hire
I want to be able to add multiple spaces using my account

As a user,
So that others can see what my space has to offer
I’d like to add a description, inc size, price

As a user
So that my space doesn’t get double-booked
I’d want to list the dates when my space is available

As a user
So that I can allow people to use my space
I want to be able to approve hire request

As a user
So that my space doesn’t get double-booked
I want booked-up dates to be automatically removed from ‘available dates’

As a user
So that no one else can edit my spaces
I want my spaces to be associated only with my account

As a user
So that I can decide whether to approve or a deny a request
I want to see details about the request

As a user
So that I can find a space to hire
I want to see a list of available spaces with available dates

As a user
So that I can decide it’s the right space for me
I’d like to see a description, inc size, price etc

As a user
So that I can book a space for the night
I want to send a booking request 

As a user
So that no-one else can use my booked space
I want my reserved date to become unavailable to others

As a user
So that I can keep track of my requests
I want to see a list of spaces I requested

As a user
So that I can keep track of my requests
I want to see space requests I’ve received

```
```
Nouns:
users, email, username, password
spaces, name, description, size, location, price, user_id
dates, date, is_available, space_id
bookings, is_confirmed, space_id, date_id, user_id(booker)



```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record        |       Properties                                            |
| ------------  | ----------------------------------------------------------- |
|  users        |    email, username, password                                |
|  spaces       |    name, description, size, location, price, user_id        |
|  dates        |    date, is_available, space_id                             |
|  bookings     |    is_confirmed, space_id, date_id, user_id(booker)         |


## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: users
id: SERIAL
email: text
username: text
password: text

Table: spaces
id: SERIAL
name: text
description: text
size: int
location: text
price: float
user_id: int foreign key

Table: dates
id: SERIAL
date: date
is_available: boolean
space_id: int foreign key

Table: bookings
id: SERIAL
is_confirmed: boolean
space_id: int foreign key
date_id: int foreign key
owner_id: int foreign key (ref user_id)
booker_id: int foreign key (ref user_id)

```

## 4. Decide on The Tables Relationship

One-to-many

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email text,
    username text,
    password text
);

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

-- Then the table with the foreign key second.
CREATE TABLE dates (
    id SERIAL PRIMARY KEY,
    date date,
    is_available boolean,
    space_id int,
    constraint fk_spaces foreign key(space_id)
    references spaces(id)
    on delete cascade
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    is_confirmed boolean,
    space_id int,
    date_id int,
    booker_id int,
    owner_id int,
    constraint fk_spaces_bookings foreign key(space_id)
    references spaces(id)
    on delete cascade,
    constraint fk_dates foreign key(date_id)
    references dates(id)
    on delete cascade,
    constraint fk_bookers foreign key(booker_id)
    references users(id)
    on delete cascade,
    constraint fk_owners foreign key(owner_id)
    references users(id)
    on delete cascade
);
```

## 6.  Create the tables

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```