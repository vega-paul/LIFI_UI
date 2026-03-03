# Page Object Model

This directory contains the Page Object Model (POM) implementation for the Jumper Exchange UI automation tests.

## Structure

### BasePage (`base-page.ts`)
The foundation class that provides common functionality used across all page objects:

- **Navigation**: `navigateTo(url)`, `waitForPageLoad()`
- **Page Information**: `getTitle()`, `getCurrentUrl()`
- **Element Interactions**: `click()`, `isVisible()`, `waitForElement()`, `getText()`
- **Popup Handling**: `waitForNewPage()`

### HomePage (`home-page.ts`)
Extends `BasePage` and provides methods specific to the Jumper Exchange home page:

- **Navigation**: `goto()`, `verifyHomePageLoaded()`
- **Tab Navigation**: `navigateThroughTabs()`, `clickPortfolio()`, `clickMissions()`, etc.
- **Menu Interactions**: `openMainMenu()`, `navigateToLearn()`, `openDiscord()`

## Usage

```typescript
import { HomePage } from '../pages';

test('example test', async ({ page }) => {
  const homePage = new HomePage(page);
  await homePage.goto();
  await homePage.verifyHomePageLoaded();
  await homePage.navigateThroughTabs();
});
```

## Best Practices

1. **Single Responsibility**: Each page object should represent one page or component
2. **Descriptive Method Names**: Methods should clearly describe what action they perform
3. **Encapsulation**: Page elements are private, only methods are exposed
4. **Inheritance**: Use `BasePage` for common functionality
5. **TypeScript**: Use proper typing for all parameters and return values

## Adding New Page Objects

1. Create a new class extending `BasePage`
2. Initialize locators in the constructor
3. Add page-specific methods
4. Export from `index.ts`
5. Update tests to use the new page object