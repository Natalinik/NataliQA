# PrometheusQAAutoLearningProject - Test Automation Project

This project contains automated tests for various websites and APIs, including GitHub, makeup.com.ua, and auto.ria.com. The tests are written using the `pytest` framework and the `selenium` library for UI testing.

## Requirements

- Python 3.7+
- `pytest`
- `selenium`
- `webdriver-manager`
- `requests`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Natalinik/NataliQA.git
    cd NataliQA
    ```
2. Install the required packages:
    ```sh
    pip install pytest
    pip install selenium
    pip install webdriver-manager
    pip install requests
    ```

## Running Tests

To run all tests:
   
```sh
pytest
```

To run tests with a specific marker:

```sh
pytest -m "http"
```

## Test Markers

The following markers are defined in the `pytest.ini` file:

- `change`: Tests that modify the user's name
- `check`: Tests that check the user's name
- `http`: Tests that check the HTTP protocol
- `api`: Tests that check the GitHub API
- `database`: Tests that check the database
- `ui`: Tests that check the GitHub UI
- `makeup`: Tests for makeup.com.ua
- `autoria`: Tests for auto.ria.com
