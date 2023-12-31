# Team Puffins' MakersBnB Python Project

## Introduction
- I made this project with Team Puffins for Makers Module 6 - Engineering Project 1
- It is based on a [Makers' seed repo](https://github.com/makersacademy/makersbnb-python-seed) 
- It is an "airbnb" style site
<img width="1440" alt="image" src="https://github.com/NatalieJClark/makersbnb-python/assets/107806810/e1a0a959-0042-4800-8772-83540d47ad57">

## Objectives
The user can:
- [x] Create an account
- [x] Log in and out
- [x] See navbar links for "Log Out", "My Spaces", "Create Space", "Manage Requests" and "My Bookings", as well as their username, when they are logged in
- [x] View all users' spaces
- [x] View the avaliable dates for a space
- [x] Book an avaliable date for a space
- [x] Create a space
- [x] View all their own spaces
- [x] View details of all booking requests for their own spaces
- [x] Confirm booking requests for their own spaces
- [x] View details of their own booking requests for a space

## Setup
```shell
# Clone the repository to your local machine
; git clone https://github.com/NatalieJClark/makersbnb-python.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py
# Now visit http://localhost:5001/login in your browser
```
## Collaborators:

With thanks to my Puffins' teammates:
- [@AigulDj](https://github.com/AigulDj)
- [@igorlangoni](https://github.com/igorlangoni)
- [@kmatheson1](https://github.com/kmatheson1)
- [@LilachD](https://github.com/LilachD)
- [@PiotrSurowiec90](https://github.com/PiotrSurowiec90)
