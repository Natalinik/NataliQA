from selenium.webdriver.common.by  import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.makeup.makeup_product_page import MakeupProductPage


class MakeupMainPage(BasePage):
    URL = "https://makeup.com.ua/ua/"
    BRAND_PROPOSALS_CLASS = "ajax-loadable-slider"
    PRODUCT_LINK_SELECTOR = "a.simple-slider-list__image"
    BASKET_COUNTER_SELECTOR = ".header-basket .header-counter"

    def __init__(self, driver: WebDriver = None) -> None:
        super().__init__(driver)

    def open(self):
        self.driver.get(MakeupMainPage.URL)

    def open_product(self, position = 0):
        brand_proposals = self.driver.find_elements(By.CLASS_NAME, MakeupMainPage.BRAND_PROPOSALS_CLASS)[0]
        wait = WebDriverWait(self.driver, timeout = 3)
        wait.until(lambda d : brand_proposals.is_displayed())

        product_link = self.driver.find_elements(By.CSS_SELECTOR, MakeupMainPage.PRODUCT_LINK_SELECTOR)[position]
        product_link.click()

        return MakeupProductPage(self.driver)

    def get_basket_products_counter(self) -> str:
        basket_counter = self.driver.find_element(By.CSS_SELECTOR, MakeupMainPage.BASKET_COUNTER_SELECTOR)
        
        return basket_counter.text
