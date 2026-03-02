# Jumper Exchange UI Automation Framework

This project contains UI automation tests for the Jumper Exchange platform using Playwright with pytest and Page Object Model (POM).

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd JumperUIAutomation
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

## Execution Instructions

### Run all tests
```bash
pytest
```

### Run tests in headed mode (visible browser)
```bash
pytest --headed
```

### Run specific test file
```bash
pytest tests/test_home_page.py
```

### Run tests in specific browser
```bash
pytest --browser chromium  # Google Chrome/Chromium
pytest --browser firefox   # Mozilla Firefox
pytest --browser webkit    # Safari (WebKit)
```

### Run tests on all browsers (parallel execution)
```bash
# CI/CD runs on Chromium and Firefox automatically
# For local multi-browser testing, run separately:
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

### Troubleshooting Browser Issues

If you encounter browser launch failures (common on macOS), try these solutions:

#### Quick Fixes
```bash
# 1. Reinstall Playwright browsers
playwright install --force

# 2. Try different browser
pytest --browser firefox
pytest --browser chrome

# 3. Run in headless mode
pytest --headed=false

# 4. Run diagnostic script
python diagnose_browser.py
```

#### Advanced Troubleshooting
- **macOS Issue**: Browser crashes with `SEGV_ACCERR` are common on macOS
- **ARM Macs**: May require Rosetta or specific browser configurations
- **Permissions**: Ensure full disk access for terminal/Python
- **Virtual Environment**: Try running outside virtual environment

### Generate HTML report
```bash
pytest --html=reports/report.html
```

### View logs
```bash
tail -f pytest.log
```

## Project Structure

```
JumperUIAutomation/
├── docs/
│   └── TestPlan.md          # Test plan and design
├── pages/
│   ├── base_page.py         # Base page class
│   └── home_page.py         # Home page POM
├── tests/
│   └── test_home_page.py    # Test specifications
├── utils/                   # Utility functions
├── reports/                 # Test reports
├── conftest.py              # Pytest configuration
├── requirements.txt         # Python dependencies
└── README.md
```

## Test Cases Covered

- Wallet Setup
- Home page navigation and tab switching
- Menu navigation to Learn section
- Menu selection of Discord

## Configuration

- **Framework:** Playwright with pytest
- **Language:** Python
- **Pattern:** Page Object Model
- **Browsers:** Chrome, Edge, Firefox
- **IDE:** VSCode configured for pytest with debugging support

## CI/CD

GitHub Actions workflow is configured to run tests on every push and pull request.

## Reports

Test results are generated in HTML format and stored in the `reports/` directory.

### Available Reports
- **HTML Test Report**: `reports/test_report.html` - Comprehensive test execution results
- **Bug Reports**: `reports/bug_report.md` - Detailed bug tracking and analysis
- **Test Logs**: `pytest.log` - Real-time test execution logs with detailed tracing

## Deliverables Status

### ✅ Completed Deliverables

1. **Test Plan** — Comprehensive test plan in `docs/TestPlan.md`
   - Scope, objectives, test cases, approach, and risk assessment

2. **Test Suite** — Complete GitHub repository at `https://github.com/vega-paul/LIFI_API`
   - Well-structured codebase with Page Object Model
   - Comprehensive logging and error handling
   - CI/CD pipeline configured

3. **Reports** — Test results and bug tracking
   - HTML test report: `reports/test_report.html`
   - Bug reports: `reports/bug_report.md`
   - Real-time logs: `pytest.log`

4. **README** — Complete setup and execution documentation
   - Installation instructions
   - Test execution commands
   - Project structure overview

5. **Bonus: CI/CD Workflow** — GitHub Actions pipeline
   - Automated testing on push/PR for all browsers (Chrome, Edge, Firefox)
   - Parallel browser execution in CI/CD
   - Separate test result artifacts for each browser

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
