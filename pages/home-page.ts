import type { Page, Locator } from "@playwright/test";
import { expect } from "@playwright/test";
import { BasePage } from "./base-page";

/**
 * Home page class containing methods specific to the Jumper Exchange home page
 */
export class HomePage extends BasePage {
  // Page elements
  private readonly jumperLogo: Locator;
  private readonly mainMenuButton: Locator;
  private readonly learnLink: Locator;
  private readonly discordLink: Locator;

  // Navigation buttons
  private readonly portfolioButton: Locator;
  private readonly missionsButton: Locator;
  private readonly earnButton: Locator;
  private readonly exchangeButton: Locator;
  private readonly connectWalletButton: Locator;

  constructor(page: Page) {
    super(page);

    // Initialize locators
    this.jumperLogo = page.locator("#jumper-logo");
    this.mainMenuButton = page.getByRole("button", { name: "Main Menu" });
    this.learnLink = page.getByRole("link", { name: "Learn" });
    this.discordLink = page.getByRole("link", { name: "Discord social link" });
    this.connectWalletButton = page.getByRole("button", { name: "Connect", exact: true });

    // Navigation buttons
    this.portfolioButton = page.getByTestId("navbar-portfolio-button");
    this.missionsButton = page.getByTestId("navbar-missions-button");
    this.earnButton = page.getByTestId("navbar-earn-button");
    this.exchangeButton = page.getByTestId("navbar-exchange-button");
  }

  /**
   * Navigate to the Jumper Exchange home page
   */
  async goto(): Promise<void> {
    await this.navigateTo("https://jumper.exchange/");
    await this.waitForPageLoad();
  }

  /**
   * Verify that the home page is loaded correctly
   */
  async verifyHomePageLoaded(): Promise<void> {
    await expect(this.page).toHaveTitle(/Jumper/);
    await expect(this.jumperLogo).toBeVisible();
  }

  /**
   * Navigate through the main navigation tabs
   */
  async navigateThroughTabs(): Promise<void> {
    await this.portfolioButton.click();
    await this.missionsButton.click();
    await this.earnButton.click();
    await this.missionsButton.click();
    await this.portfolioButton.click();
    await this.exchangeButton.click();
  }

  /**
   * Open the main menu
   */
  async openMainMenu(): Promise<void> {
    await this.mainMenuButton.click();
  }

  /**
   * Navigate to the Learn section from the menu
   */
  async navigateToLearn(): Promise<void> {
    await this.openMainMenu();
    await this.learnLink.click();
    await expect(this.page).toHaveURL("https://jumper.exchange/learn");
  }

  /**
   * Open Discord from the menu
   * @returns The Discord page that opens in a new tab
   */
  async openDiscord(): Promise<Page> {
    await this.openMainMenu();

    // Wait for the popup to open
    const pagePromise = this.waitForNewPage();

    await this.discordLink.click();

    const discordPage = await pagePromise;

    // Verify we're on Discord
    await discordPage.getByRole("textbox", { name: "Display Name" }).click();
    await discordPage.getByText("You've been invited to join").click();

    return discordPage;
  }

  /**
   * Click on the portfolio navigation button
   */
  async clickPortfolio(): Promise<void> {
    await this.portfolioButton.click();
  }

  /**
   * Click on the missions navigation button
   */
  async clickMissions(): Promise<void> {
    await this.missionsButton.click();
  }

  /**
   * Click on the earn navigation button
   */
  async clickEarn(): Promise<void> {
    await this.earnButton.click();
  }

  /**
   * Click on the exchange navigation button
   */
  async clickExchange(): Promise<void> {
    await this.exchangeButton.click();
  }

  /**
   * Click on the connect wallet button
   */
  async connectWallet(): Promise<void> {
    await this.connectWalletButton.click();
  }
};
