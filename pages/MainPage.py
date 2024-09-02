from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from constants import SHOP_URL


class MainPage:
    def __init__(self, chrome: WebDriver):
        self.chrome = chrome
        self.chrome.get(SHOP_URL)
        self.actions = ActionChains(self.chrome)

    def hide_sticky_box(self, value: str):
        self.chrome.find_element(By.CLASS_NAME, value).click()

    def select_from_menu(self, select_1, select_2, select_3):
        self.actions.move_to_element(select_1)
        self.actions.move_to_element(select_2)
        self.actions.move_to_element(select_3).click()
        self.actions.perform()

    def men_menu_locator(self, value: str):
        return self.chrome.find_element(By.ID, value)

    def men_tops_locator(self, value: str):
        return self.chrome.find_element(By.ID, value)

    def men_hoodies_sweatshirts_locator(self, value: str):
        return self.chrome.find_element(By.ID, value)

    def women_menu_locator(self, value: str):
        return self.chrome.find_element(By.ID, value)

    def women_bottoms_locator(self, value: str):
        return self.chrome.find_element(By.ID, value)

    def women_pants_locator(self, value: str):
        return self.chrome.find_element(By.ID, value)