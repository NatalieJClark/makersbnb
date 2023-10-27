from playwright.sync_api import Page, expect
import time
from flask import session


# Tests for your routes go here

"""
We can render the login page
"""
def test_get_login(page, test_web_address):
    # We load a virtual browser and navigate to the /login page
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/login")

    h5_tag = page.locator('h5')
    login_tag = page.locator('.login-btn')

    expect(h5_tag).to_have_text("Login Here")
    expect(login_tag).to_have_text("Login")

def test_link_create_user(page, test_web_address):
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/login")
    page.click("text=New to MakersBNB?")
    h5_tag = page.locator('h5')
    expect(h5_tag).to_have_text("Create New User")

def test_user_create_match_passwords(page, test_web_address):
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/users/new")
    page.fill("input[name=email]", "email@email.co")
    page.fill("input[name=username]", "new_user")
    page.fill("input[name=password1]", "e1234x")
    page.fill("input[name=password2]", "e1234x")
    page.locator(".btn").click()
    h5_tag = page.locator('h5')
    expect(h5_tag).to_have_text("Login Here")

def test_user_create_no_password_match(page, test_web_address):
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/users/new")
    page.fill("input[name=email]", "email@email.co")
    page.fill("input[name=username]", "new_user")
    page.fill("input[name=password1]", "e1234x")
    page.fill("input[name=password2]", "e123456")
    page.locator(".btn").click()
    error_tag = page.locator('.t-password-error')
    expect(error_tag).to_have_text("*Your passwords don't match. Please try again.")

def test_user_login_successfully(page, test_web_address):
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email]", "name3@cmail.com")
    page.fill("input[name=password]", "password3")
    page.locator(".btn").click()
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('Welcome to Makers B&B')

def test_user_login_wrong_email(page, test_web_address):
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email]", "name10@cmail.com")
    page.fill("input[name=password]", "password3")
    page.locator(".btn").click()
    error_tag = page.locator('.t-login-error')
    expect(error_tag).to_have_text("*Email and Password don't match. Please try again.")

def test_user_login_wrong_password(page, test_web_address):
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email]", "name1@cmail.com")
    page.fill("input[name=password]", "password3")
    page.locator(".btn").click()
    error_tag = page.locator('.t-login-error')
    expect(error_tag).to_have_text("*Email and Password don't match. Please try again.")


"""
When we are successfully logged in
We want the navbar to show 'log out' instead of 'log in'
"""
def test_navbar_logout(page, test_web_address):
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email]", "name3@cmail.com")
    page.fill("input[name=password]", "password3")
    page.locator(".btn").click()
    logout_tag = page.locator('.t-logout')
    expect(logout_tag).to_have_text('Log Out')

"""
When we click log-out, our session ends
"""
# def test_logout_ends_session(page, test_web_address):
#     page.set_default_timeout(1000)
#     page.goto(f"http://{test_web_address}/login")
#     page.fill("input[name=email]", "name3@cmail.com")
#     page.fill("input[name=password]", "password3")
#     page.locator(".btn").click()
#     page.click("text=Log Out")
#     assert dict(session) == {}
    

def test_detail_view(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email]", "name3@cmail.com")
    page.fill("input[name=password]", "password3")
    page.locator(".btn").click()
    page.goto(f"http://{test_web_address}/spaces/detail/1")
    name_tag = page.locator('.card-title')
    expect(name_tag).to_have_text('MYPLACE1 £10.00')

    dates = page.locator('.list-group-item')
    expect(dates).to_have_text(['2023-10-29', '2023-10-30'])
    
def test_list_view(page, test_web_address, db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')

    page.goto(f"http://{test_web_address}/home")
    title_tag = page.locator('.t-test')
    expect(title_tag).to_have_text(
        ['MYPLACE1 £10.00', 'MYPLACE2 £15.00', 'MYPLACE3 £20.00', 'MYPLACE4 £30.00', 'MYPLACE5 £18.00']
        )

def test_list_spaces_by_user_id(page, test_web_address, db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email]", "name1@cmail.com")
    page.fill("input[name=password]", "password1")
    page.locator(".btn").click()
    page.goto(f"http://{test_web_address}/users/1/spaces")
    title_tag = page.locator('.card-title')
    expect(title_tag).to_have_text(['MYPLACE1 £10.00', 'MYPLACE2 £15.00'])

def test_see_more_button(page, test_web_address, db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email]", "name3@cmail.com")
    page.fill("input[name=password]", "password3")
    page.locator(".btn").click()

    page.locator('.btn-primary').first    
    page.click("text=See more")
    title_tag = page.locator('.card-title')
    expect(title_tag).to_have_text('MYPLACE1 £10.00')

def test_request_list(page, test_web_address, db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email]", "name3@cmail.com")
    page.fill("input[name=password]", "password3")
    page.locator(".btn").click()
    page.goto(f"http://{test_web_address}/user/requests")
    test_class = page.locator('.test-requests')
    expect(test_class).to_have_text('Guest Email')

def test_my_bookings(page, test_web_address, db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email]", "name3@cmail.com")
    page.fill("input[name=password]", "password3")
    page.locator(".btn").click()
    page.goto(f"http://{test_web_address}/user/mybookings")
    test_class = page.locator('.test-bookings')
    expect(test_class).to_have_text('Owner Email')

def test_request_list_confirm(page, test_web_address, db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name=email]", "name2@cmail.com")
    page.fill("input[name=password]", "password2")
    page.locator(".btn").click()
    page.goto(f"http://{test_web_address}/user/requests")
    page.locator(".btn").click()
    test_confirmed = page.locator('.test-confirmed')
    expect(test_confirmed).to_have_text('True')

# def test_create_space(page, test_web_address, db_connection):
#     """
    
#     """

#     db_connection.seed('seeds/makers_bnb_library.sql')
#     page.set_default_timeout(1000)
#     page.goto(f"http://{test_web_address}/login")
#     page.fill("input[name=email]", "name3@cmail.com")
#     page.fill("input[name=password]", "password3")
#     page.locator(".btn").click()

    
#     page.goto(f"http://{test_web_address}/spaces/new")
#     page.fill("input[name=name]", "New space 1")
#     page.fill("textarea[name=description]", "New space Description 1")
#     page.fill("input[name=size]", "20")
#     page.fill("input[name=location]", "London")
#     page.fill("input[name=price]", "75")
#     page.locator(".btn").click()
#     page.screenshot(path='screenshot.png')
#     title_tag = page.locator('.t-test')

#     expect(title_tag).to_have_text([
#         'MYPLACE4 £30.00', 
#         'MYPLACE5 £18.00',
#         'NEW SPACE 1 £75.00']
#         )

