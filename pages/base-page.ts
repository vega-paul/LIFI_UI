import type { Page, Locator } from '@playwright/test';

/**
 * Base page class containing common functionality for all page objects
 */
export class BasePage {
  protected page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  /**
   * Navigate to a specific URL
   * @param url - The URL to navigate to
   */
  async navigateTo(url: string): Promise<void> {
    await this.page.goto(url);
  }

  /**
   * Wait for the page to load completely
   */
  async waitForPageLoad(): Promise<void> {
    await this.page.waitForLoadState('networkidle');
  }

  /**
   * Get the current page title
   * @returns The page title
   */
  async getTitle(): Promise<string> {
    return await this.page.title();
  }

  /**
   * Get the current page URL
   * @returns The current URL
   */
  async getCurrentUrl(): Promise<string> {
    return this.page.url();
  }

  /**
   * Click on an element
   * @param locator - The element locator
   */
  async click(locator: Locator): Promise<void> {
    await locator.click();
  }

  /**
   * Check if an element is visible
   * @param locator - The element locator
   * @returns True if visible, false otherwise
   */
  async isVisible(locator: Locator): Promise<boolean> {
    return await locator.isVisible();
  }

  /**
   * Wait for an element to be visible
   * @param locator - The element locator
   * @param timeout - Timeout in milliseconds (default: 5000)
   */
  async waitForElement(locator: Locator, timeout: number = 5000): Promise<void> {
    await locator.waitFor({ state: 'visible', timeout });
  }

  /**
   * Get text content of an element
   * @param locator - The element locator
   * @returns The text content
   */
  async getText(locator: Locator): Promise<string> {
    return await locator.textContent() || '';
  }

  /**
   * Wait for a new page to open (popup)
   * @returns Promise that resolves to the new page
   */
  async waitForNewPage(): Promise<Page> {
    return await this.page.waitForEvent('popup');
  }
}