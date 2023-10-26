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

def test_detail_view(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces/detail/1")
    name_tag = page.locator('.card-title')
    expect(name_tag).to_have_text('MYPLACE1 £10.0')

    dates = page.locator('.list-group-item')
    expect(dates).to_have_text(['2023-10-29', '2023-10-30'])
    
def test_list_view(page, test_web_address, db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')

    page.goto(f"http://{test_web_address}/spaces/list")
    title_tag = page.locator('.card-title')
    expect(title_tag).to_have_text(
        ['MYPLACE1 £10.0', 'MYPLACE2 £15.0', 'MYPLACE3 £20.0', 'MYPLACE4 £30.0', 'MYPLACE5 £18.0']
        )

def test_list_spaces_by_user_id(page, test_web_address, db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')

    page.goto(f"http://{test_web_address}/users/1/spaces")
    title_tag = page.locator('.card-title')
    expect(title_tag).to_have_text(['MYPLACE1 £10.0', 'MYPLACE2 £15.0'])


def test_see_more_button(page, test_web_address, db_connection):
    db_connection.seed('seeds/makers_bnb_library.sql')

    page.goto(f"http://{test_web_address}/spaces/list")
    page.locator('.btn-primary').first    
    page.click("text=See more")
    title_tag = page.locator('.card-title')
    expect(title_tag).to_have_text('MYPLACE1 £10.0')