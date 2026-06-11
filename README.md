# Playwright Python BDD Automation Framework

## Overview

This project is an End-to-End Test Automation Framework built using:

* Playwright
* Python
* Pytest
* Pytest-BDD
* Allure Reporting
* Page Object Model (POM)

## Features

* End-to-End Order Workflow Automation
* BDD Implementation using Gherkin
* Dynamic Order ID Validation
* Allure Reporting
* Screenshot Capture on Failure
* Reusable Page Object Model

## Project Structure


project
│
├── pages
├── features
├── step_definitions
├── tests
├── reports
├── conftest.py
├── config.py
├── pytest.ini
└── README.md


## Installation


pip install -r requirements.txt


## Run Tests


pytest -v

## Run BDD Tests


pytest step_definitions -v


## Generate Allure Report


pytest --alluredir=reports
allure serve reports

## Technologies Used

* Python
* Playwright
* Pytest
* Pytest-BDD
* Allure
* GitHub

## Author

Sagar
