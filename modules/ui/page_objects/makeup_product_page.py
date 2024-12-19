from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by  import By

class MakeupProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def buy_product(self):
        btn_buy = self.driver.find_element(By.CSS_SELECTOR, ".product-item__button .buy")
        btn_buy.click()

    def close_basket_popup(self):
        close_icon = self.driver.find_element(By.CSS_SELECTOR, ".popup__window .popup-close.close-icon")
        close_icon.click()

    def go_to_main_page(self):
        logo = self.driver.find_element(By.CLASS_NAME, "backgroundless-logo")
        logo.click()
