from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait

from modules.ui.page_objects.base_page import BasePage


class MakeupProductPage(BasePage):
    BUY_BUTTON_SELECTOR = ".product-item__button .buy"
    POPUP_WINDOW_CLASS = "popup__window"
    CLOSE_ICON_SELECTOR = ".popup__window .popup-close.close-icon"
    LOGO_CLASS = "logo"

    def __init__(self, driver):
        super().__init__(driver)

    def buy_product(self):
        btn_buy = self.driver.find_element(By.CSS_SELECTOR, MakeupProductPage.BUY_BUTTON_SELECTOR)
        btn_buy.click()

    def close_basket_popup(self):
        popup_window = self.driver.find_element(By.CLASS_NAME, MakeupProductPage.POPUP_WINDOW_CLASS)
        wait = WebDriverWait(self.driver, timeout = 2)
        wait.until(lambda d : popup_window.is_displayed())

        close_icon = self.driver.find_element(By.CSS_SELECTOR, MakeupProductPage.CLOSE_ICON_SELECTOR)
        close_icon.click()

    def go_to_main_page(self):
        logo = self.driver.find_element(By.CLASS_NAME, MakeupProductPage.LOGO_CLASS)
        logo.click()

    def buy_product_and_go_to_main_page(self):
        self.buy_product()
        self.close_basket_popup()
        self.go_to_main_page()
