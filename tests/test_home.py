import pytest
from pages.home_page import HomePage


def test_home_page(setup_browser):
    driver = setup_browser
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    page = HomePage(driver)

    # ======= Radio Button =======
    assert page.select_radio("radio3")
