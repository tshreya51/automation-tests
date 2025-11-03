import pytest
from utilities.driver_factory import get_chrome_driver

@pytest.fixture()
def setup_browser():
    driver=get_chrome_driver()
    yield driver
    driver.quit()