import pytest
import logging
from pages.home_page import HomePage

logger = logging.getLogger(__name__)

@pytest.fixture
def home_page(page):
    logger.info("Setting up HomePage fixture")
    home_page = HomePage(page)
    home_page.open()
    logger.info("HomePage opened successfully")
    return home_page

def test_wallet_setup_happy_path(home_page):
    logger.info("Starting wallet setup test")
    # Test wallet setup
    home_page.setup_wallet()
    # Add assertions
    assert home_page.is_visible('[data-testid="wallet-connected"]')
    logger.info("Wallet setup test completed")

def test_navigate_home_page_switch_tabs(home_page):
    logger.info("Starting tab navigation test")
    # Switch to different tabs
    home_page.switch_tab('Swap')  # Example tab
    assert 'swap' in home_page.page.url
    logger.debug("Switched to Swap tab")

    home_page.switch_tab('Bridge')  # Example tab
    assert 'bridge' in home_page.page.url
    logger.debug("Switched to Bridge tab")
    logger.info("Tab navigation test completed")

def test_open_menu_navigate_learn(home_page):
    logger.info("Starting learn navigation test")
    home_page.navigate_to_learn()
    # Assert navigation to learn page
    assert 'learn' in home_page.page.url
    logger.info("Learn navigation test completed")

def test_open_menu_select_discord(home_page):
    logger.info("Starting Discord selection test")
    with home_page.page.context.expect_page() as new_page_info:
        home_page.select_discord()
    new_page = new_page_info.value
    assert 'discord' in new_page.url
    logger.info("Discord selection test completed")
