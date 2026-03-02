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
pytest --browser chromium
```

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
- **Browsers:** Chromium, Firefox, WebKit

## CI/CD

GitHub Actions workflow is configured to run tests on every push and pull request.

## Reports

Test results are generated in HTML format and stored in the `reports/` directory.

## Notes

- Selectors are placeholders and should be updated based on actual site inspection.
- Tests are designed for happy path scenarios.
- External dependencies like wallet connections may require additional setup for full execution.
