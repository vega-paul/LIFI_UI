import pytest
from pages.home_page import HomePage

@pytest.fixture
def home_page(page):
    home_page = HomePage(page)
    home_page.open()
    return home_page

def test_wallet_setup_happy_path(home_page):
    # Test wallet setup
    home_page.setup_wallet()
    # Add assertions
    assert home_page.is_visible('[data-testid="wallet-connected"]')

def test_navigate_home_page_switch_tabs(home_page):
    # Switch to different tabs
    home_page.switch_tab('Swap')  # Example tab
    assert 'swap' in home_page.page.url

    home_page.switch_tab('Bridge')  # Example tab
    assert 'bridge' in home_page.page.url

def test_open_menu_navigate_learn(home_page):
    home_page.navigate_to_learn()
    # Assert navigation to learn page
    assert 'learn' in home_page.page.url

def test_open_menu_select_discord(home_page):
    with home_page.page.context.expect_page() as new_page_info:
        home_page.select_discord()
    new_page = new_page_info.value
    assert 'discord' in new_page.url