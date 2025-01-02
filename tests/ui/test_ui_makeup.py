import pytest

from modules.ui.page_objects.makeup_main_page import MakeupMainPage


@pytest.mark.ui
@pytest.mark.makeup
def test_basket_one_product_counter(makeup_main_page):
    # Open the first product
    product_page = makeup_main_page.open_product(0)

    product_page.buy_product()
    product_page.close_basket_popup()
    product_page.go_to_main_page()

    assert makeup_main_page.check_basket_products_counter(1)


@pytest.mark.ui
@pytest.mark.makeup
def test_basket_several_products_counter(makeup_main_page):
    for i in range(2):
        # Open and buy the first and the next products
        product_page = makeup_main_page.open_product(i)
        product_page.buy_product_and_go_to_main_page()

    assert makeup_main_page.check_basket_products_counter(2)
