from selenium.webdriver.common.by  import By
from selenium.webdriver.remote.webdriver import WebDriver


class AutoRiaFuelCalculatorWidget:
    FUEL_PRICE_SELECTOR = ".fuel-calc .fuelPrice"
    FUEL_EXPENSE_SELECTOR = ".fuel-calc .expense"
    DISTANCE_SELECTOR = ".fuel-calc .distance"
    CALCULATE_BUTTON_SELECTOR = ".fuel-calc .button"
    RESULT_EXPENSE_SELECTOR = ".fuel-calc .commonExpense"
    RESULT_PRICE_SELECTOR = ".fuel-calc .price"

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def fill_fuel_price(self, fuel_price):
        fuel_price_elem = self.driver.find_element(By.CSS_SELECTOR, AutoRiaFuelCalculatorWidget.FUEL_PRICE_SELECTOR)
        fuel_price_elem.send_keys(fuel_price)

    def fill_fuel_expense(self, liters_per_100_km):
        fuel_expense_elem = self.driver.find_element(By.CSS_SELECTOR, AutoRiaFuelCalculatorWidget.FUEL_EXPENSE_SELECTOR)
        fuel_expense_elem.send_keys(liters_per_100_km)

    def fill_distance(self, distance_km):
        distance_elem = self.driver.find_element(By.CSS_SELECTOR, AutoRiaFuelCalculatorWidget.DISTANCE_SELECTOR)
        distance_elem.send_keys(distance_km)

    def calculate(self):
        calculate_button = self.driver.find_element(By.CSS_SELECTOR, AutoRiaFuelCalculatorWidget.CALCULATE_BUTTON_SELECTOR)
        calculate_button.click()

    def get_result_expense(self):
        result_expense_elem = self.driver.find_element(By.CSS_SELECTOR, AutoRiaFuelCalculatorWidget.RESULT_EXPENSE_SELECTOR)
        
        return result_expense_elem.text
    
    def get_result_price(self):
        result_price_elem = self.driver.find_element(By.CSS_SELECTOR, AutoRiaFuelCalculatorWidget.RESULT_PRICE_SELECTOR)
        
        return result_price_elem.text
    