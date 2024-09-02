from selenium import webdriver
import pytest


@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()