# Jumper Exchange UI Automation Framework

This project contains UI automation tests for the Jumper Exchange platform using Playwright and Page Object Model (POM).

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd JumperUIAutomation
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Install Playwright browsers:**
   ```bash
   npx playwright install
   ```

## Execution Instructions

### Run all tests
```bash
npx playwright test
```

### Run tests in headed mode (visible browser)
```bash
npx playwright test --headed
```

### Run specific test file
```bash
npx playwright test tests/homePageTests.spec.js
```

### Run tests in specific browser
```bash
npx playwright test --project=chromium
```

### Generate HTML report
```bash
npx playwright show-report
```

## Project Structure

```
JumperUIAutomation/
├── docs/
│   └── TestPlan.md          # Test plan and design
├── pages/
│   ├── BasePage.js          # Base page class
│   └── HomePage.js          # Home page POM
├── tests/
│   └── homePageTests.spec.js # Test specifications
├── utils/                   # Utility functions
├── reports/                 # Test reports
├── package.json
└── README.md
```

## Test Cases Covered

- Wallet Setup
- Home page navigation and tab switching
- Menu navigation to Learn section
- Menu selection of Discord

## Configuration

- **Framework:** Playwright
- **Language:** JavaScript
- **Pattern:** Page Object Model
- **Browsers:** Chromium, Firefox, WebKit

## CI/CD

GitHub Actions workflow is configured to run tests on every push and pull request.

## Reports

Test results are generated in HTML format and stored in the `reports/` directory.

## Notes

- Selectors are placeholders and should be updated based on actual site inspection.
- Tests are designed for happy path scenarios.
- External dependencies like wallet connections may require additional setup for full execution.