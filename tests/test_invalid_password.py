import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators
from data.urls import BASE_URL


@pytest.mark.usefixtures("driver")
class TestInvalidPassword:
    def test_password_failure(self, driver, invalid_password):
        login_page = LoginPage(driver)
        login_page.open(BASE_URL + "login")
        login_page.login(invalid_password["email"], invalid_password["password"])
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        # Проверка только в assert
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()
