import { test } from "@playwright/test";
import { HomePage } from "../pages";

test.describe("Jumper Exchange Home Page", () => {
  let homePage: HomePage;

  test.beforeEach(async ({ page }) => {
    homePage = new HomePage(page);
    await homePage.goto();
    await homePage.verifyHomePageLoaded();
  });

  test("navigate through home page and switch tabs", async () => {
    await homePage.navigateThroughTabs();
  });

  test("open menu and navigate through learn", async () => {
    await homePage.navigateToLearn();
  });

  test("open menu and select discord", async () => {
    await homePage.openDiscord();
  });
})
