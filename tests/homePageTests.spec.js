const { test, expect } = require('@playwright/test');
const HomePage = require('../pages/HomePage');

test.describe('Jumper Exchange UI Tests', () => {
  let homePage;

  test.beforeEach(async ({ page }) => {
    homePage = new HomePage(page);
    await homePage.open();
  });

  test('Wallet Setup - Happy Path', async () => {
    // Test wallet setup
    await homePage.setupWallet();
    // Add assertions
    expect(await homePage.isVisible('[data-testid="wallet-connected"]')).toBeTruthy();
  });

  test('Navigate through home page and switch tabs', async () => {
    // Switch to different tabs
    await homePage.switchTab('Swap'); // Example tab
    expect(await homePage.page.url()).toContain('swap');

    await homePage.switchTab('Bridge'); // Example tab
    expect(await homePage.page.url()).toContain('bridge');
  });

  test('Open menu and navigate through "learn"', async () => {
    await homePage.navigateToLearn();
    // Assert navigation to learn page
    expect(await homePage.page.url()).toContain('learn');
  });

  test('Open menu and select discord', async () => {
    await homePage.selectDiscord();
    // Assert discord link or page
    // Since discord opens external, check if new tab or something
    const [newPage] = await Promise.all([
      homePage.page.context().waitForEvent('page'),
      homePage.selectDiscord()
    ]);
    expect(newPage.url()).toContain('discord');
  });
});