import pytest

from modules.ui.page_objects.sign_in_page import SignInPage


@pytest.mark.ui
def test_check_incorrect_username_page_object(github_sign_in_page):
    # we are trying to log in to GitHub
    github_sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Check that the page name is what we expect
    assert github_sign_in_page.check_title("Sign in to GitHub · GitHub")
