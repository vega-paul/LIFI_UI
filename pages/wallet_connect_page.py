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

        if wallet_name == "Rabby Wallet":
            logger.info("Selecting Rabby Wallet - clicking installed selector")
            installed_selector = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@id='widget-wallet-modal-content']/div[@class='MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered mui-1cbf1l2']/div[@class='MuiCollapse-wrapper MuiCollapse-vertical mui-15830to']/div[@class='MuiCollapse-wrapperInner MuiCollapse-vertical mui-9vd5ud']/div[@class='MuiList-root MuiList-padding mui-vnvcgk']/div[2]/..//span[@class='MuiChip-label MuiChip-labelMedium mui-14vsv3w'][normalize-space()='Installed']"
            with self.page.expect_popup() as self.popup_info:
                self.page.click(installed_selector)
                logger.info("Clicked installed selector, waiting for popup")

    def connect_rabby_wallet_extension(self):
        """Handle Rabby Wallet Chrome extension popup connection"""
        logger.info("Handling Rabby Wallet extension popup connection")
        try:
            # Wait for the extension popup
            extension_popup = self.page.wait_for_event("popup", timeout=10000)
            logger.info("Rabby Wallet extension popup detected")

            # Wait for popup to load
            extension_popup.wait_for_load_state()
            logger.info("Extension popup loaded")

            # Click the Connect button using the provided selectors
            # Try multiple selectors in case the DOM structure changes
            connect_clicked = False

            # Try aria selector first
            try:
                extension_popup.get_by_role("button", name="Connect").click()
                connect_clicked = True
                logger.info("Clicked Connect button using aria selector")
            except Exception as e:
                logger.warning(f"Connect button aria selector failed: {e}")

            # Try CSS selector if aria failed
            if not connect_clicked:
                try:
                    extension_popup.locator("button.mb-0 > span").click()
                    connect_clicked = True
                    logger.info("Clicked Connect button using CSS selector")
                except Exception as e:
                    logger.warning(f"Connect button CSS selector failed: {e}")

            # Try XPath selector as last resort
            if not connect_clicked:
                try:
                    extension_popup.locator("//*[@id='root']/div/div/div/div/div[2]/div/div[2]/button[1]/span").click()
                    connect_clicked = True
                    logger.info("Clicked Connect button using XPath selector")
                except Exception as e:
                    logger.error(f"All Connect button selectors failed: {e}")
                    raise Exception("Could not find Connect button in Rabby Wallet extension popup")

            if connect_clicked:
                logger.info("Successfully connected to Rabby Wallet via extension")
            else:
                raise Exception("Failed to click Connect button in extension popup")

        except Exception as e:
            logger.error(f"Failed to handle Rabby Wallet extension popup: {e}")
            raise

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

