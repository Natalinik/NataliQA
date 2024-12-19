from modules.ui.page_objects.makeup_main_page import MakeupMainPage
from modules.ui.page_objects.makeup_product_page import MakeupProductPage
import pytest
import time

@pytest.mark.ui
@pytest.mark.makeup
def test_basket_products_counter():
    main_page = MakeupMainPage()
    main_page.open()
    
    product_page = main_page.open_product(0)

    product_page.buy_product()
    product_page.close_basket_popup()
    product_page.go_to_main_page()

    assert main_page.check_basket_products_counter(1)

    main_page.open_product(1)

    product_page.buy_product()
    product_page.close_basket_popup()
    product_page.go_to_main_page()

    assert main_page.check_basket_products_counter(2)

    main_page.close()