import pytest


@pytest.mark.ui
@pytest.mark.autoria
def test_auto_ria_fuel_calculator(auto_ria_fuel_price_page):
    fuel_calc = auto_ria_fuel_price_page.fuel_calculator_widget
    fuel_calc.fill_fuel_price("59.99")
    fuel_calc.fill_fuel_expense("7")
    fuel_calc.fill_distance("300")
    fuel_calc.calculate()

    # After clicking in the widget, there are two results, so we check both
    assert fuel_calc.get_result_expense() == "21.0"
    assert fuel_calc.get_result_price() == "1259.8"
    