import time
import pytest
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators

URL_LOGIN = "https://stellarburgers.education-services.ru/login"

@pytest.mark.usefixtures("driver")
class TestInvalidPassword:
    def test_password_failure(self, driver, invalid_password):
        login_page = LoginPage(driver)
        login_page.open(URL_LOGIN)
        login_page.login(invalid_password["email"], invalid_password["password"])
        time.sleep(2)
        # Ожидаем, что кнопка "Войти" всё ещё отображается (вход не выполнен)
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()