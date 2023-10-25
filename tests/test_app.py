from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
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


    # # We look at the <p> tag
    # strong_tag = page.locator("p")

    # # We assert that it has the text "This is the homepage."
    # expect(strong_tag).to_have_text("This is the homepage.")

"""
"""