import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ✅ 1. Убираем локальный путь, используем webdriver_manager (универсально для всех)
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


# ✅ 2. Статичные данные выносим в константы (не фикстуры)
VALID_USER = {
    "email": "anastassiya_makiyenko_32_991@gmail.com",
    "password": "zxc123"
}

INVALID_PASSWORD = {
    "email": "anastassiya_makiyenko_32_991@gmail.com",
    "password": "wrongpass"
}