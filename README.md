# Online Shopping Project

## Description

This project is designed for testing the functionality of men's *Hoodies & Sweatshirts* and women's *Pants* categories of a
Magento-based website. The project uses Selenium WebDriver for browser automation and `pytest` for writing and
executing test cases. The testing is done on the Google Chrome browser.

## Development Environment

- ***IDE:*** PyCharm Community Edition 2024.2
- ***Python Version:*** 3.12
- ***Test Framework:*** `pytest==8.2.2`
- ***Web Driver:*** Google ChromeDriver
- ***Browser Version:*** Google Chrome 128

## Project Structure

The project is organized as follows:

### 1. `constants.py`

This file contains constants used throughout the project. Currently, it defines the URL for the website:

```python
SHOP_URL = "https://magento.softwaretestingboard.com/"
```

### 2. `pages/MainPage.py`

This file contains a class with methods to interact with the main page of the website and with the menu bar and hiding
the sticky box.

### 3. `pages/ClothesCategory.py`

This file includes methods for selecting and interacting with different types of clothing items for men and women. 
It is specifically designed to test the clothing categories and their functionalities.

### 4. `pages/ShippingAddress.py`

This file contains methods to fill in necessary fields for the shipping during the checkout process

### 5. `test/conftest.py`

This file is used to define shared fixtures and setup code for the `pytest` framework. In this project, it contains 
the configuration for the Chrome WebDriver:

```python
@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()
```
### 6. `test/test_shop.py`

This file contains the actual test cases that use the methods from the pages directory to perform automated testing
on the website. It utilizes the fixtures defined in `conftest.py` to manage the WebDriver instance.

## Dependencies and Imports

This project relies on Selenium WebDriver for browser automation.
Below are the specific imports used within the project:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest
```

## Setup Instructions

`Make sure you have installed Python 3.12 and Google Chrome version 128`

### 1. Clone the repository to your local machine:

```
git clone <repository-url>
```

### 2. Navigate to the project directory:

```
cd <project-directory>
```

### 3. Install all required dependencies, use the following command:

```
pip install -r requirements.txt
```

### 4. Run the test cases using pytest:

```
pytest
```
### 5. Run the test cases using pytest to get more information:

```
pytest -v
```

## Warnings

It seems when you run `test_women_clothes`, sometimes for unknown reason appears 'Attention' message. This happens 
when you delete pants from the cart. Evidence will be found in `test/screenshot.png`
