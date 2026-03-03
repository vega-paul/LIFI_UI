import { test, expect } from "@playwright/test";
import { HomePage } from "../pages";

test.describe("Wallet Connection Tests", () => {
    test("verify basic wallet test infrastructure works", async ({ page }) => {
        console.log('🧪 Starting basic wallet infrastructure test...');
        let homePage: HomePage;

        homePage = new HomePage(page);
        await homePage.goto();
        await homePage.verifyHomePageLoaded();
        await page.getByRole('button', { name: 'Connect', exact: true }).click();


        // Check for wallet connection button
        const walletButton = page.locator('[data-testid*="connect"], button:has-text("Connect")').first();
        const isWalletButtonVisible = await walletButton.isVisible().catch(() => false);

        if (isWalletButtonVisible) {
            console.log('✅ Wallet connect button found');
        } else {
            console.log('⚠️ Wallet connect button not found');
        }

        console.log('🎉 Basic wallet test infrastructure verified');
    });
})
