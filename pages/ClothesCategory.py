from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ClothesCategory:
    def __init__(self, chrome: WebDriver):
        self.chrome = chrome
        self.actions = ActionChains(self.chrome)

    def men_product_item_list(self, time_out: int,):
        page_hoodies_sweatshirts = WebDriverWait(self.chrome, time_out).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-item-link")))
        all_clothes = len(page_hoodies_sweatshirts)
        return str(all_clothes)

    def show_per_page(self, select_per_page: int, text_in_element: str):
        WebDriverWait(self.chrome, 1).until(EC.text_to_be_present_in_element(
            (By.XPATH, f"(//select[@id='limiter']/*[@value='{select_per_page}'])[2]"), text_in_element))
        text =  self.chrome.find_element(
            By.XPATH, f"(//select[@id='limiter']/*[@value={select_per_page}])[2]").text
        return text

    def click_on_item(self, time_out: int,  value: str):
        WebDriverWait(self.chrome, time_out).until(EC.element_to_be_clickable((By.XPATH, value))).click()

    def add_quantity(self, value: str, send_keys: str):
        self.chrome.find_element(By.ID, value).clear()
        self.chrome.find_element(By.ID, value).send_keys(send_keys)

    def get_attribute(self, value: str, attribute: str):
        return self.chrome.find_element(By.XPATH, value).get_attribute(attribute)

    def sort_by_cheapest(self, time_out: int, value: str):
        WebDriverWait(self.chrome, time_out).until(EC.element_to_be_clickable((By.XPATH, value))).click()

    def select_clothes(self, time_out: int, value: str):
        WebDriverWait(self.chrome, time_out).until(EC.element_to_be_clickable((By.ID, value))).click()

    def select_size(self,time_out: int, value: str):
        WebDriverWait(self.chrome, time_out).until(EC.element_to_be_clickable((By.XPATH, value))).click()

    def select_color(self, time_out: int, value: str):
        WebDriverWait(self.chrome, time_out).until(EC.element_to_be_clickable((By.XPATH, value))).click()

    def button_add_to_cart(self, value: str):
       self.actions.move_to_element(self.chrome.find_element(By.XPATH, value)).click().perform()

    def cart_counter(self, time_out: int, text_in_element: str, value: str):
        WebDriverWait(self.chrome, time_out).until(EC.text_to_be_present_in_element(
            (By.XPATH, value), text_in_element))
        counter_text = self.chrome.find_element(By.XPATH, value).text
        return counter_text

    def remove_from_cart(self, value: str):
        self.chrome.find_element(By.XPATH, value).click()

    def click_on_cart(self, value: str):
        self.chrome.find_element(By.CLASS_NAME, value).click()

    def click_pop_up(self, time_out: int, value: str):
        WebDriverWait(self.chrome, time_out).until(EC.element_to_be_clickable((By.CSS_SELECTOR, value))).click()
        self.chrome.find_element(By.CSS_SELECTOR, value).click()

    def button_proceed_to_checkout(self, time_out: int, value: str):
        WebDriverWait(self.chrome, time_out).until(EC.element_to_be_clickable((By.ID, value))).click()