import logging
from .base_page import BasePage

logger = logging.getLogger(__name__)

class WalletConnectPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        logger.info("Initializing WalletConnectPage")
        # Wallet connection modal selectors
        self.wallet_modal = '[role="dialog"]'
        self.close_button = '[data-testid="wallet-modal-close"]'

        # MetaMask container object - the installed wallets section
        self.metamask_container = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@id='widget-wallet-modal-content']/div[@class='MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered mui-1cbf1l2']/div[@class='MuiCollapse-wrapper MuiCollapse-vertical mui-15830to']/div[@class='MuiCollapse-wrapperInner MuiCollapse-vertical mui-9vd5ud']/div[@class='MuiList-root MuiList-padding mui-vnvcgk']/div[2]"

        # Common parent locator for wallet options
        self.wallet_options_container = "div.MuiCard-root.mui-udv5zg"
        self.common_parent = self.page.locator("div.MuiCard-root.mui-udv5zg")

        # MetaMask specific selector - will use text-based selection
        # The CSS selector provided uses unsupported :contains() and :has() pseudo-selectors

        # Modal close button
        self.modal_close_button = "div.MuiDialog-root button:nth-of-type(2) > svg"
        logger.info("WalletConnectPage initialized successfully")

    def is_wallet_modal_open(self) -> bool:
        """Check if the wallet connection modal is open"""
        is_open = self.is_visible(self.wallet_modal)
        logger.info(f"Wallet modal open status: {is_open}")
        return is_open

    def select_wallet(self, wallet_name: str):
        """Select a wallet using text-based selection or specific selectors"""
        logger.info(f"Attempting to select wallet: {wallet_name}")
        if not self.is_wallet_modal_open():
            logger.error("Wallet modal is not open - cannot select wallet")
            raise Exception("Wallet modal is not open")

        if wallet_name == "Abstract":
            logger.info("Selecting Abstract wallet - clicking installed selector")
            installed_selector = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@id='widget-wallet-modal-content']/div[@class='MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered mui-1cbf1l2']/div[@class='MuiCollapse-wrapper MuiCollapse-vertical mui-15830to']/div[@class='MuiCollapse-wrapperInner MuiCollapse-vertical mui-9vd5ud']/div[@class='MuiList-root MuiList-padding mui-vnvcgk']/div[1]/..//span[normalize-space()='Installed']"
            with self.page.expect_popup() as self.popup_info:
                self.page.click(installed_selector)
                logger.info("Clicked installed selector, waiting for popup")

    def close_wallet_popup(self):
        logger.info("Closing wallet authentication popup")
        auth_popup = self.popup_info.value
        auth_popup.wait_for_load_state()
        logger.info("Popup loaded, closing it")
        auth_popup.close()
        logger.info("Wallet authentication popup closed")
        
   

    def close_wallet_modal(self):
        """Close the wallet connection modal using the close button from recording"""
        logger.info("Attempting to close wallet modal")
        try:
            # Try the close button from the recording first
            logger.info("Trying modal close button from recording")
            self.page.click(self.modal_close_button)
            logger.info("Successfully closed wallet modal using recording button")
        except Exception as e:
            logger.warning(f"Recording close button failed: {e}, trying fallback")
            # Fallback to the original close button
            if self.is_wallet_modal_open():
                self.click(self.close_button)
                logger.info("Successfully closed wallet modal using fallback button")
            else:
                logger.info("Wallet modal already closed")

    def get_available_wallets(self) -> list:
        """Get list of available wallets in the modal"""
        logger.info("Getting available wallets from modal")
        if not self.is_wallet_modal_open():
            logger.warning("Wallet modal is not open - cannot get available wallets")
            return []

        # Find all wallet options in the MetaMask container section
        logger.info("Querying wallet elements in MetaMask container")
        wallet_elements = self.page.query_selector_all(f"{self.metamask_container}//span")
        wallets = []
        for element in wallet_elements:
            wallet_name = element.text_content().strip()
            if wallet_name:
                wallets.append(wallet_name)
        logger.info(f"Found {len(wallets)} available wallets: {wallets}")
        return wallets

