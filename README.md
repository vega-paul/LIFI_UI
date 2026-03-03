# Jumper Exchange UI Automation Framework

This project contains UI automation tests for the Jumper Exchange platform using Playwright with TypeScript.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd JumperUIAutomation
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Install Playwright browsers:**
   ```bash
   npx playwright install
   ```

4. **Setup Wallet Extensions (for wallet tests):**
   ```bash
   # Create extensions directory
   mkdir -p extensions/coinbase

   # Download Coinbase Wallet extension from Chrome Web Store
   # Visit: https://chromewebstore.google.com/detail/coinbase-wallet-extension/hnfanknocfeofbddgcijnmhnfnkdnaad
   # Download the .crx file and rename it to .zip, then extract to:
   # extensions/coinbase/hnfanknocfeofbddgcijnmhnfnkdnaad/[version]/

   # Alternative: Use a pre-configured extension directory
   # The test will provide clear error messages if extensions are missing
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
npx playwright test e2e/jumper.spec.ts
```

### Run tests in specific browser
```bash
npx playwright test --project=chromium  # Google Chrome/Chromium
npx playwright test --project=firefox   # Mozilla Firefox
npx playwright test --project=webkit    # Safari (WebKit)
```

### Run tests on all browsers (parallel execution)
```bash
# CI/CD runs on Chromium and Firefox automatically (Linux-compatible)
# For local multi-browser testing, run separately:
npx playwright test --project=chromium  # Linux/macOS/Windows
npx playwright test --project=firefox   # Linux/macOS/Windows
npx playwright test --project=webkit    # macOS only (not available on Linux CI/CD)
```

### Troubleshooting Browser Issues

If you encounter browser launch failures (common on macOS), try these solutions:

#### Quick Fixes
```bash
# 1. Reinstall Playwright browsers
npx playwright install --force

# 2. Try different browser
npx playwright test --project=firefox
npx playwright test --project=chromium

# 3. Run in headless mode
npx playwright test --headed=false
```

#### Advanced Troubleshooting
- **macOS Issue**: Browser crashes with `SEGV_ACCERR` are common on macOS
- **ARM Macs**: May require Rosetta or specific browser configurations
- **Permissions**: Ensure full disk access for terminal/Node.js

### Generate HTML report
```bash
npx playwright show-report
```

### View test results
```bash
npx playwright test --reporter=line
```

## Project Structure

```
JumperUIAutomation/
├── docs/
│   └── TestPlan.md          # Test plan and design
├── e2e/
│   ├── jumper.spec.ts       # Home page test specifications
│   └── wallet.spec.ts       # Wallet connection test specifications
├── pages/
│   ├── base-page.ts         # Base page class with common functionality
│   ├── home-page.ts         # Home page object with page-specific methods
│   └── index.ts             # Page object exports
├── wallet-setup/
│   └── metamask.setup.ts    # MetaMask wallet setup utilities
├── fixtures.ts              # Playwright test fixtures
├── playwright-report/       # HTML test reports
├── test-results/            # Screenshots, videos, and traces
├── reports/
│   └── test_report.html     # Additional test reports
├── playwright.config.ts     # Playwright configuration
├── package.json             # Node.js dependencies
└── README.md
```

## Test Cases Covered

### Home Page Tests (`e2e/jumper.spec.ts`)
- Navigate to Jumper Exchange home page
- Verify home page loads correctly
- Navigate through main navigation tabs (Portfolio, Missions, Earn, Exchange)
- Open main menu and navigate to Learn section
- Open main menu and select Discord (opens in new tab)

### Wallet Connection Tests (`e2e/wallet.spec.ts`)
- Verify basic wallet test infrastructure
- Navigate to home page and verify loading
- Check for wallet connection button presence
- Basic wallet connection workflow validation

## Configuration

- **Framework:** Playwright with @playwright/test
- **Language:** TypeScript
- **Browsers:** Chromium (Chrome), Firefox (CI/CD), WebKit (macOS local only)
- **IDE:** VSCode configured for TypeScript and Playwright

## CI/CD

GitHub Actions workflow is configured to run tests on every push and pull request to main/master branches.

### CI Features
- **Automated Testing**: Runs on Ubuntu Linux with Chromium browser
- **Headless Execution**: Tests run in headless mode for CI efficiency
- **System Dependencies**: Installs required Linux libraries for browser support
- **Website Accessibility Check**: Verifies Jumper Exchange site is accessible before testing
- **Comprehensive Reporting**: Generates HTML and JSON test reports
- **Artifact Upload**: Saves test results, screenshots, videos, and traces as downloadable artifacts
- **Error Handling**: Continues workflow even if tests fail, ensuring reports are always generated

### Workflow Triggers
- Push to `main` or `master` branches
- Pull requests to `main` or `master` branches

### Test Environment
- **OS**: Ubuntu Latest
- **Node.js**: Version 20
- **Browser**: Chromium (Chrome)
- **Test Runner**: 1 worker (sequential execution in CI)

## Reports

Test results are generated in HTML format and stored in the `playwright-report/` directory.

### Available Reports
- **HTML Test Report**: `playwright-report/index.html` - Comprehensive test execution results
- **Bug Reports**: `reports/bug_report.md` - Detailed bug tracking and analysis

## Deliverables Status

### ✅ Completed Deliverables

1. **Test Plan** — Comprehensive test plan in `docs/TestPlan.md`
   - Scope, objectives, test cases, approach, and risk assessment

2. **Test Suite** — Complete GitHub repository at `https://github.com/vega-paul/LIFI_UI.git`
   - Well-structured codebase with TypeScript and Playwright
   - Comprehensive logging and error handling
   - CI/CD pipeline configured

3. **Reports** — Test results and bug tracking
   - HTML test report: `playwright-report/index.html`
   - Bug reports: `reports/bug_report.md`

4. **README** — Complete setup and execution documentation
   - Installation instructions
   - Test execution commands
   - Project structure overview

5. **Bonus: CI/CD Workflow** — GitHub Actions pipeline
   - Automated testing on push/PR with Chromium browser
   - Headless execution with comprehensive error handling
   - Test artifacts uploaded (HTML reports, screenshots, traces)

### 🔧 Current Issues

- **Browser Launch Failures**: Playwright browsers crash on startup (environment-specific)
- **Modal Detection Timeouts**: Wallet modal detection needs selector updates
- **Selector Stability**: Current selectors are placeholders requiring site inspection

### 📋 Next Steps

1. Resolve browser environment issues
2. Update selectors based on actual Jumper Exchange site inspection
3. Implement more robust waiting strategies
4. Add blockchain-specific test scenarios

## Notes

- Selectors are placeholders and should be updated based on actual site inspection.
- Tests are designed for happy path scenarios.
- External dependencies like wallet connections may require additional setup for full execution.
