import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from data.users import VALID_USER, INVALID_PASSWORD


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def valid_user():
    return VALID_USER


@pytest.fixture
def invalid_password():
    return INVALID_PASSWORD
