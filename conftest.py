import pytest

from modules.api.clients.github import GitHub
from modules.ui.page_objects.makeup.makeup_main_page import MakeupMainPage
from modules.ui.page_objects.github.sign_in_page import SignInPage
from modules.ui.page_objects.auto_ria.auto_ria_fuel_price_page import AutoRiaFuelPricePage


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Natalia"
        self.second_name = "Platonova"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    github = GitHub()

    yield github


@pytest.fixture
def makeup_main_page():
    main_page = MakeupMainPage()
    main_page.open()

    yield main_page

    main_page.close()


@pytest.fixture
def github_sign_in_page():
    # Creating a page object
    sign_in_page = SignInPage()
    # Open the page https://github.com/login
    sign_in_page.open()

    yield sign_in_page

    # Close the browser
    sign_in_page.close()


@pytest.fixture
def auto_ria_fuel_price_page():
    # Creating a page object
    fuel_price_page = AutoRiaFuelPricePage()
    # Open the page https://auto.ria.com/uk/toplivo/
    fuel_price_page.open()

    yield fuel_price_page

    # Close the browser
    fuel_price_page.close()
    