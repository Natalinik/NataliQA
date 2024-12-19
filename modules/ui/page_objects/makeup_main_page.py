from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.makeup_product_page import MakeupProductPage
from selenium.webdriver.common.by  import By

class MakeupMainPage(BasePage):
    URL = "https://makeup.com.ua/ua/"

    def __init__(self):
        super().__init__()

    def open(self):
        self.driver.implicitly_wait(5)
        self.driver.get(MakeupMainPage.URL)

    def open_product(self, position = 0):
        product_link = self.driver.find_elements(By.CSS_SELECTOR, "a.simple-slider-list__image")[position]
        product_link.click()
        return MakeupProductPage(self.driver)

    def buy_product(self):
        btn_buy = self.driver.find_element(By.CSS_SELECTOR, ".product-item__button .buy")
        btn_buy.click()

    def close_basket_popup(self):
        close_icon = self.driver.find_element(By.CSS_SELECTOR, ".popup__window .popup-close.close-icon")
        close_icon.click()

    def go_to_main_page(self):
        logo = self.driver.find_element(By.CLASS_NAME, "backgroundless-logo")
        logo.click()

    def check_basket_products_counter(self, expected_products_number):
        basket_counter = self.driver.find_element(By.CSS_SELECTOR, ".header-basket .header-counter")
        return int(basket_counter.text) == expected_products_number
    