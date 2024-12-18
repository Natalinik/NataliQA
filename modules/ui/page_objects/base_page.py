from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:

    def __init__(self, driver = None) -> None:
        self.driver = driver or webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def close(self):
        self.driver.close()
