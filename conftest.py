import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CHROMEDRIVER_PATH = "C:/WebDriver/bin/chromedriver.exe"


@pytest.fixture
def driver():
    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def valid_user():
    return {
        "email": "anastassiya_makiyenko_32_991@gmail.com",
        "password": "zxc123"
    }


@pytest.fixture
def invalid_password():
    return {
        "email": "anastassiya_makiyenko_32_991@gmail.com",
        "password": "wrongpass"
    }