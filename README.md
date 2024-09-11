# HRM Web Application Automation Test Suite

This project provides an automation test suite for a sample HRM web application using **Playwright** for browser automation, **API testing**, and **Allure Report** for test reporting. The suite follows a modular design using the **Page Object Model (POM)** and is written in **Python**.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [How to Run Tests](#how-to-run-tests)
5. [Generating Allure Reports](#generating-allure-reports)
6. [Test Cases Description](#test-cases-description)

## Requirements

Ensure you have the following installed on your system:
- Python 3.7+
- Allure command-line tool (for generating test reports)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sekel_tech/hrm-automation.git
   cd hrm-automation

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt

3. Install Playwright browser binaries:
    ```bash
    playwright install

## Project Structure

project/<br/>
│<br/>
├── config/<br/>
│   └── config.py        &nbsp;&nbsp;              # Configuration details (URLs, credentials)<br/>
│<br/>
├── pages/<br/>
│   ├── login_page.py      &nbsp;&nbsp;            # Page Object for login page<br/>
│   ├── dashboard_page.py    &nbsp;&nbsp;          # Page Object for dashboard and user actions<br/>
│<br/>
├── api/<br/>
│   └── api_utils.py        &nbsp;&nbsp;           # Utility functions for API testing<br/>
│<br/>
├── tests/<br/>
│   ├── test_login.py       &nbsp;&nbsp;           # Test case for login<br/>
│   ├── test_user_search.py   &nbsp;&nbsp;         # Test case for user search<br/>
│   ├── test_add_user.py      &nbsp;&nbsp;         # Test case for adding a user<br/>
│   ├── test_api.py          &nbsp;&nbsp;          # Test case for API testing<br/>
│<br/>
├── pytest.ini             &nbsp;&nbsp;            # pytest configurations<br/>
└── requirements.txt       &nbsp;&nbsp;            # Python dependencies<br/>

## How to RUN Tests

1. Run the entire test suite using pytest:
    ```bash
    pytest

2. To run a specific test file:
    ```bash
    pytest tests/test_login.py

3. To run tests with browser UI visible (non-headless):
    ```bash
    pytest --headed

## Generating Allure Reports

1. Run the tests and store the results for Allure:
    ```bash
    pytest --alluredir=allure-results

2. Generate and view the report:
    ```bash
    allure serve allure-results

## Test Cases Description
1. **Test Case 1: User Login** <br/>
    - Automates the login functionality.<br/>
    - Checks if a user-specific element is present after login.

2. **Test Case 2: User Management Search**<br/>
    - Automates searching for a user in the user management section.<br/>
    - Verifies if the search results contain the correct user.

3. **Test Case 3: Add a New User**<br/>
    - Automates the process of adding a new user in the system.<br/>
    - Checks if the user is added successfully.
    

4. **Test Case 4: API Testing**<br/>
    - Sends a GET request to fetch users and validates the response status and data structure.