import time
import logging
from playwright.sync_api import Page

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.load_time_threshold = 10.0  # seconds

    def navigate(self, url: str):
        """Navigate to URL and measure load time"""
        logger.info(f"🔗 Starting navigation to: {url}")
        start_time = time.time()

        try:
            logger.info(f"📡 Executing page.goto({url})")
            self.page.goto(url)
            logger.info(f"⏳ Waiting for networkidle state")
            self.page.wait_for_load_state('networkidle')
            logger.info(f"✅ Page load state reached")

            load_time = time.time() - start_time
            logger.info(f"⏱️  Page loaded in {load_time:.2f} seconds")

            # Validate page load time
            if load_time >= self.load_time_threshold:
                logger.warning(f"⚠️  Page load time {load_time:.2f}s exceeded threshold {self.load_time_threshold}s")
            else:
                logger.info(f"✅ Page load time {load_time:.2f}s within threshold {self.load_time_threshold}s")

            assert load_time < self.load_time_threshold, f"Page load time {load_time:.2f}s exceeded {self.load_time_threshold}s threshold"
            return load_time
        except Exception as e:
            load_time = time.time() - start_time
            logger.error(f"❌ Navigation failed after {load_time:.2f}s: {e}")
            raise

    def wait_for_load(self):
        """Wait for page to load completely"""
        self.page.wait_for_load_state('networkidle')

    def click(self, selector: str):
        """Click element after verifying visibility"""
        self.assert_element_visible(selector)
        logger.info(f"Clicking element: {selector}")
        self.page.click(selector)

    def type_text(self, selector: str, text: str):
        """Type text after verifying element visibility"""
        self.assert_element_visible(selector)
        logger.info(f"Typing text into: {selector}")
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        """Get text content after verifying element visibility"""
        self.assert_element_visible(selector)
        return self.page.text_content(selector)

    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        try:
            return self.page.locator(selector).is_visible()
        except Exception:
            return False

    def assert_element_visible(self, selector: str, timeout: int = 5000):
        """Assert that element is visible within timeout"""
        try:
            locator = self.page.locator(selector)
            locator.wait_for(state='visible', timeout=timeout)
            assert locator.is_visible(), f"Element {selector} is not visible"
            logger.info(f"Element verified visible: {selector}")
        except Exception as e:
            logger.error(f"Element visibility check failed for {selector}: {e}")
            raise AssertionError(f"Element {selector} is not visible within {timeout}ms")

    def measure_page_load_time(self, url: str) -> float:
        """Measure and return page load time"""
        start_time = time.time()
        self.page.goto(url)
        self.page.wait_for_load_state('networkidle')
        load_time = time.time() - start_time
        return load_time

    def validate_url_contains(self, expected_text: str):
        """Validate that current URL contains expected text"""
        current_url = self.page.url
        assert expected_text.lower() in current_url.lower(), f"URL '{current_url}' does not contain '{expected_text}'"
        logger.info(f"URL validation passed: {current_url} contains '{expected_text}'")

    def validate_page_title(self, expected_title: str = None):
        """Validate page title"""
        title = self.page.title()
        if expected_title:
            assert expected_title.lower() in title.lower(), f"Page title '{title}' does not contain '{expected_title}'"
        else:
            assert title and len(title.strip()) > 0, "Page title is empty"
        logger.info(f"Page title validated: {title}")
        return title
