# QA Automation Portfolio
Portfolio for QA Automation projects

## Setup

### Install Dependencies
```bash
# Create and activate virtual environment (if not already done)
python3 -m venv .venv
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### Install Web Testing Dependencies
```bash
# Navigate to web test directory and install Node.js dependencies
cd tests/web
npm install
npx playwright install
```

## Running Tests

### Python Tests (API & Unit)
```bash
# Activate virtual environment
source .venv/bin/activate


# Run all Python tests
pytest

# Run specific test files
pytest tests/api/test_users_api.py -v
pytest tests/Unit/test_fixtures_demo.py -v

# Run tests with coverage
pytest --cov=tests --cov-report=html
```

### Web Tests (Playwright)
```bash
cd tests/web

# Run all Playwright tests
npx playwright test

# Run tests with UI
npx playwright test --ui

# Run specific test
npx playwright test example.spec.ts

# Open last HTML report run
npx playwright show-report
```


### Alternative: Run Python Tests Without Activation
```bash
# From project root, use venv Python directly
./.venv/bin/python -m pytest tests/api/test_users_api.py -v
./.venv/bin/python -m pytest tests/ -v
```

## Project Structure
```
├── tests/
│   ├── conftest.py          # Global pytest configuration
│   ├── api/                 # API tests (Python/requests)
│   ├── Unit/                # Unit tests (Python/pytest)
│   └── web/                 # Web UI tests (Playwright/TypeScript)
├── docs/                    # Documentation and notes
├── requirements.txt         # Python dependencies
└── README.md               # This file
```
