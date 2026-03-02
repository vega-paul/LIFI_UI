from .base_page import BasePage

class WalletPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Wallet connection selectors
        self.connect_wallet_button = '[data-testid="connect-wallet-button"]'
        self.wallet_options_modal = '[data-testid="wallet-options-modal"]'
        self.installed_wallets_section = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@id='widget-wallet-modal-content']/div[@class='MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered mui-1cbf1l2']/div[@class='MuiCollapse-wrapper MuiCollapse-vertical mui-15830to']/div[@class='MuiCollapse-wrapperInner MuiCollapse-vertical mui-9vd5ud']/div[@class='MuiList-root MuiList-padding mui-vnvcgk']/div[1]/..//span[normalize-space()='Installed']"
        self.disconnect_button = '[data-testid="disconnect-wallet"]'

        # Wallet info selectors
        self.wallet_address = '[data-testid="wallet-address"]'
        self.wallet_balance = '[data-testid="wallet-balance"]'
        self.connected_wallet_indicator = '[data-testid="connected-wallet-indicator"]'

        # Transaction selectors
        self.transaction_history = '[data-testid="transaction-history"]'
        self.transaction_item = '[data-testid="transaction-item"]'

    def connect_wallet(self, wallet_name: str = "MetaMask"):
        """Connect a wallet from the installed wallets section"""
        self.click(self.connect_wallet_button)
        self.wait_for_load()

        # Wait for wallet modal to appear
        self.page.wait_for_selector(self.installed_wallets_section, timeout=10000)

        # Click on the specified wallet from installed wallets
        wallet_xpath = f"{self.installed_wallets_section}/ancestor::div[contains(@class, 'MuiList-root')]/following-sibling::div//span[normalize-space()='{wallet_name}']"
        self.page.click(wallet_xpath)

        # Wait for connection to complete
        self.page.wait_for_selector(self.connected_wallet_indicator, timeout=30000)

    def disconnect_wallet(self):
        """Disconnect the currently connected wallet"""
        self.click(self.disconnect_button)
        self.wait_for_load()
        # Verify wallet is disconnected
        assert not self.is_wallet_connected()

    def is_wallet_connected(self) -> bool:
        """Check if a wallet is currently connected"""
        return self.is_visible(self.connected_wallet_indicator)

    def get_wallet_address(self) -> str:
        """Get the connected wallet address"""
        if self.is_wallet_connected():
            return self.get_text(self.wallet_address)
        return ""

    def get_wallet_balance(self) -> str:
        """Get the wallet balance"""
        if self.is_wallet_connected():
            return self.get_text(self.wallet_balance)
        return "0"

    def get_transaction_history(self) -> list:
        """Get list of recent transactions"""
        if not self.is_visible(self.transaction_history):
            return []

        transaction_elements = self.page.query_selector_all(self.transaction_item)
        transactions = []
        for element in transaction_elements:
            transactions.append(element.text_content())
        return transactions

    def switch_to_wallet_tab(self):
        """Switch to wallet tab if available"""
        # This might be called from home page or other pages
        self.page.click('[data-testid="wallet-tab"]')

    def wait_for_wallet_connection(self, timeout: int = 30000):
        """Wait for wallet connection to complete"""
        self.page.wait_for_selector(self.connected_wallet_indicator, timeout=timeout)