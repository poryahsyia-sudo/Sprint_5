import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import (
    MainPageLocators,
    LoginPageLocators,
    AccountPageLocators,
)
from data.urls import BASE_URL
from utils.generator import generate_email, generate_password


@pytest.mark.usefixtures("driver", "valid_user")
class TestLoginFlow:
    def wait(self, driver, locator):
        return WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def test_login_opens_account(self, driver, valid_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        self.wait(driver, LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        assert self.wait(driver, AccountPageLocators.PROFILE_BUTTON).is_displayed()

    def test_constructor_button_returns_home(self, driver, valid_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        self.wait(driver, LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        assert self.wait(driver, AccountPageLocators.PROFILE_BUTTON).is_displayed()
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        assert self.wait(driver, LoginPageLocators.ORDER_BUTTON).is_displayed()

    def test_logo_redirects_to_home(self, driver, valid_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        self.wait(driver, LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        assert self.wait(driver, AccountPageLocators.PROFILE_BUTTON).is_displayed()
        driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
        assert self.wait(driver, LoginPageLocators.ORDER_BUTTON).is_displayed()

    def test_logout_redirects_to_login(self, driver, valid_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        self.wait(driver, LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        assert self.wait(driver, AccountPageLocators.PROFILE_BUTTON).is_displayed()
        driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains("login"))
        assert "login" in driver.current_url