from .base_page import BasePage
from .wallet_connect_page import WalletConnectPage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = 'https://jumper.exchange'  # Update with actual URL if different
        self.menu_button = "//button[@id='main-burger-menu-button']//*[name()='svg']"
        self.tabs = '[data-testid="tab"]'  # Placeholder for tabs
        self.connect_wallet_button = 'p:has-text("Connect")'

    def open(self):
        """Open home page with load time validation"""
        load_time = self.navigate(self.url)
        self.validate_page_title()  # Ensure page has a title
        return load_time

    def switch_tab(self, tab_name: str):
        """Switch to different navigation tabs using proper ARIA roles"""
        if tab_name.lower() == 'exchange':
            self.page.get_by_role("link", name="Exchange").click()
        elif tab_name.lower() == 'portfolio':
            self.page.get_by_role("button", name="Portfolio").click()
        elif tab_name.lower() == 'missions':
            self.page.get_by_role("button", name="Missions").click()
        elif tab_name.lower() == 'earn':
            self.page.get_by_role("button", name="Earn").click()
        else:
            # Fallback to text-based selection for other tabs
            self.page.click(f'text={tab_name}')

    def open_menu(self):
        self.click(self.menu_button)

    def navigate_to_learn(self):
        self.open_menu()
        self.page.get_by_text("Learn", exact=True).click()

    def select_discord(self):
        self.open_menu()
        self.page.locator("//a[@aria-label='Discord social link']//*[name()='svg']").click()

    def setup_wallet(self) -> WalletConnectPage:
        """Open wallet connection modal and return WalletConnectPage instance"""
        self.click(self.connect_wallet_button)
        self.wait_for_load()

        # Wait for wallet modal to appear
        wallet_connect = WalletConnectPage(self.page)
        wallet_connect.page.locator(wallet_connect.wallet_modal).wait_for(timeout=10000)

        return wallet_connect
