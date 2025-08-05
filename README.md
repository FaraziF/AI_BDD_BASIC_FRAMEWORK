# AI_BDD_BASIC_FRAMEWORK

A Behavior-Driven Development (BDD) framework that leverages Python, Playwright, Behave, Allure, and OpenAI for automated web application testing.

---

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/FaraziF/AI_BDD_BASIC_FRAMEWORK.git
    cd AI_BDD_BASIC_FRAMEWORK
    ```

2. **Create and Activate a Virtual Environment (Recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    If `requirements.txt` is missing, install manually:
    ```bash
    pip install behave playwright allure-behave openai
    ```

4. **Install Playwright Browsers**
    ```bash
    playwright install
    ```

5. **Set Up Configuration Files**
    - Create `config/openai_key.json` with your OpenAI API key:
      ```json
      { "api_key": "YOUR_OPENAI_API_KEY" }
      ```
    - Create `config/env.json` for browser settings:
      ```json
      {
        "browser": "chromium",
        "headless": false
      }
      ```

---

## Usage

### 1. **Generating Feature Scenarios (Optional)**
Automatically generate Gherkin scenarios for the "Contact Us" form:
```bash
python run_tests.py
```
This will generate or update `features/contact_form.feature`.

### 2. **Running Tests**
Execute BDD tests and generate Allure result files:
```bash
python custom_runner.py
```
- Cleans/creates `reports` and `screenshots` folders.
- Runs all scenarios tagged with `@regression`.
- Outputs results to `reports/allure-results`.

### 3. **Viewing Allure Reports**
Generate and open the Allure HTML report:
```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

---

## Project Structure

- `features/` - Gherkin feature files and step definitions.
- `features/steps/` - Python step implementations for Behave.
- `features/environment.py` - Hooks for setup/teardown (browser, Playwright).
- `config/` - Configuration files (`openai_key.json`, `env.json`, etc).
- `utils/` - Utility modules (OpenAI integration, step analysis, types).
- `run_tests.py` - Script to generate Gherkin scenarios using OpenAI.
- `custom_runner.py` - Custom test runner with Allure integration.

---

## Notes

- **Edit or add feature files** in `features/`.
- **Step definitions** are in `features/steps/contact_us_form_steps.py`.
- **OpenAI Integration:** Used for scenario and step suggestion/generation.
- **Allure Reporting:** Screenshots and test results are integrated with Allure.

---

## Requirements

- Python 3.8+
- [Playwright](https://playwright.dev/python/docs/intro)
- [Behave](https://behave.readthedocs.io/en/stable/)
- [Allure](https://docs.qameta.io/allure/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)

---

## License

[MIT](LICENSE)
