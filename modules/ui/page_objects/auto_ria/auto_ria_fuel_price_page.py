from selenium.webdriver.remote.webdriver import WebDriver

from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.auto_ria.auto_ria_fuel_calculator_widget import AutoRiaFuelCalculatorWidget


class AutoRiaFuelPricePage(BasePage):
    URL = "https://auto.ria.com/uk/toplivo/"

    def __init__(self, driver: WebDriver = None) -> None:
        super().__init__(driver)
        self.fuel_calculator_widget = AutoRiaFuelCalculatorWidget(self.driver)

    def open(self):
        self.driver.get(AutoRiaFuelPricePage.URL)
