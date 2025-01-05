from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver = None) -> None:
        self.driver = driver or webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def close(self):
        self.driver.close()
