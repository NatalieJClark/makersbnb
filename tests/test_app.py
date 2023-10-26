from playwright.sync_api import Page, expect
import time

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_login(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    h5_tag = page.locator('h5')
    login_tag = page.locator('.login-btn')

    expect(h5_tag).to_have_text("Login Here")
    expect(login_tag).to_have_text("Login")

def test_link_create_user(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")
    page.click("text=New to MakersBNB?")
    h5_tag = page.locator('h5')
    expect(h5_tag).to_have_text("Create New User")

def test_user_create_match_passwords(page, test_web_address):
    page.goto(f"http://{test_web_address}/users/new")
    page.fill("input[name=email]", "email@email.co")
    page.fill("input[name=username]", "new_user")
    page.fill("input[name=password1]", "e1234x")
    page.fill("input[name=password2]", "e1234x")
    page.locator(".btn").click()
    h5_tag = page.locator('h5')
    expect(h5_tag).to_have_text("Login Here")

def test_user_create_no_password_match(page, test_web_address):
    page.goto(f"http://{test_web_address}/users/new")
    page.fill("input[name=email]", "email@email.co")
    page.fill("input[name=username]", "new_user")
    page.fill("input[name=password1]", "e1234x")
    page.fill("input[name=password2]", "e123456")
    page.locator(".btn").click()
    error_tag = page.locator('.t-password-error')
    expect(error_tag).to_have_text("*Your passwords don't match. Please try again.")

# def test_user_login_successfully(page, test_web_address):
#     page.goto(f"http>//{test_web_address}/index")
#     page.fill("input[name=email]", "name3@cmail.com")
#     page.fill("input[name=password]", "password3")
#     page.locator(".btn").click()
#     h1_tag = page.locator('h1')
#     expecte(h1_tag).to_have_text('Welcome to Makers B&B')