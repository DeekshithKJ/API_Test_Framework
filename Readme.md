# API Test Framework

## Overview

This project is a test framework designed to test REST APIs. The framework supports GET, POST, PUT, and DELETE requests. It includes a test to validate if the key `autoident` has the correct browser matrix support for web considering the minimum version supported on each platform.

## Project Structure

- `framework/`
  - `__init__.py`: Initializes the framework module.
  - `api_client.py`: Contains the `APIClient` class for making API requests.
  - `config.py`: Stores configuration settings (e.g., base URL).

- `tests/`
  - `__init__.py`: Initializes the tests module.
  - `test_api.py`: Contains unit tests for the `APIClient`.

- `main.py`: Entry point for running tests.
- `Readme.md`: Project documentation.

## How to Run Tests

1. Ensure all dependencies are installed:
   ```sh
   pip install -r requirements.txt
