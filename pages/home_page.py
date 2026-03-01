from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = 'https://jumper.exchange'  # Update with actual URL if different
        self.menu_button = '[data-testid="menu-button"]'  # Placeholder selector
        self.tabs = '[data-testid="tab"]'  # Placeholder for tabs

    def open(self):
        self.navigate(self.url)
        self.wait_for_load()

    def switch_tab(self, tab_name: str):
        # Assuming tabs have text or data attributes
        self.page.click(f'text={tab_name}')

    def open_menu(self):
        self.click(self.menu_button)

    def navigate_to_learn(self):
        self.open_menu()
        self.page.click('text=Learn')  # Placeholder

    def select_discord(self):
        self.open_menu()
        self.page.click('text=Discord')  # Placeholder

    def setup_wallet(self):
        # Placeholder for wallet setup
        self.page.click('[data-testid="wallet-connect"]')
        # Add steps for wallet connection