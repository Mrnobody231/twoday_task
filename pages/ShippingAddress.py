from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class ShippingAddress:
    def __init__(self, chrome: WebDriver):
        self.chrome = chrome
        self.actions = ActionChains(self.chrome)

    def insert_data(self, time_out: int, element_value: str, data):
        WebDriverWait(self.chrome, time_out).until(EC.visibility_of_element_located(
            (By.XPATH, element_value))).send_keys(data)

    def find_element_with_action(self, time_out: int, value: str):
        WebDriverWait(self.chrome, time_out).until(EC.presence_of_element_located((By.XPATH, value)))
        element = self.chrome.find_element(By.XPATH, value)
        self.actions.move_to_element(element).perform()

    def scroll_to_element(self, time_out: int, value: str, text: str):
        WebDriverWait(self.chrome, time_out).until(EC.presence_of_element_located((By.XPATH, value)))
        drop_down = Select(self.chrome.find_element(By.XPATH, value))
        drop_down.select_by_visible_text(text)

    def wait(self, time_out: int, value: str):
        WebDriverWait(self.chrome, time_out).until(EC.visibility_of_element_located((By.XPATH, value)))