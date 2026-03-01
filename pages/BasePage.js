class BasePage {
  constructor(page) {
    this.page = page;
  }

  async navigate(url) {
    await this.page.goto(url);
  }

  async waitForLoad() {
    await this.page.waitForLoadState('networkidle');
  }

  async click(selector) {
    await this.page.click(selector);
  }

  async type(selector, text) {
    await this.page.fill(selector, text);
  }

  async getText(selector) {
    return await this.page.textContent(selector);
  }

  async isVisible(selector) {
    return await this.page.isVisible(selector);
  }
}

module.exports = BasePage;