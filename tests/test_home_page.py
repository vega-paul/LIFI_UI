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

def test_navigate_home_page_switch_tabs(home_page):
    logger.info("Starting tab navigation test")
    # Switch to different navigation tabs
    home_page.switch_tab('Exchange')
    logger.debug("Switched to Exchange tab")

    home_page.switch_tab('Portfolio')
    logger.debug("Switched to Portfolio tab")

    home_page.switch_tab('Missions')
    logger.debug("Switched to Missions tab")

    home_page.switch_tab('Earn')
    logger.debug("Switched to Earn tab")
    logger.info("Tab navigation test completed")

def test_open_menu_navigate_learn(home_page):
    logger.info("Starting learn navigation test")
    initial_url = home_page.page.url
    home_page.navigate_to_learn()
    # Assert that we remain on the same page (Learn opens content/modal on same page)
    home_page.page.wait_for_timeout(1000)  # Wait for any UI transitions
    assert home_page.page.url == initial_url + "learn"
    logger.info("Learn navigation test completed")

def test_open_menu_select_discord(home_page):
    logger.info("Starting Discord selection test")
    with home_page.page.context.expect_page() as new_page_info:
        home_page.select_discord()
    new_page = new_page_info.value
    assert 'discord' in new_page.url
    logger.info("Discord selection test completed")
