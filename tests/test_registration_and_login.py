import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.generator import generate_email, generate_password
from pages.locators import (
    MainPageLocators,
    RegistrationPageLocators,
    LoginPageLocators,
    PasswordRecoveryPageLocators,
)
from data.urls import BASE_URL


TIMEOUT = 3  # единое время ожидания


def wait_for(driver, locator):
    """Ожидание видимости элемента"""
    return WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(locator)
    )


@pytest.mark.usefixtures("driver")
class TestRegistrationAndLogin:
   

    def test_successful_registration(self, driver):
        driver.get(BASE_URL)
        wait_for(driver, MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        wait_for(driver, ("link text", "Зарегистрироваться")).click()
        email = generate_email()
        password = generate_password()
        wait_for(driver, RegistrationPageLocators.NAME_FIELD).send_keys("Test User")
        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        wait_for(driver, LoginPageLocators.LOGIN_BUTTON)
        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wait_for(driver, LoginPageLocators.ORDER_BUTTON)
        assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()

    def test_login_from_main_page(self, driver, valid_user):
        driver.get(BASE_URL)
        wait_for(driver, MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        wait_for(driver, LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wait_for(driver, LoginPageLocators.ORDER_BUTTON)
        assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()

    def test_login_via_personal_account(self, driver, valid_user):
        driver.get(BASE_URL)
        wait_for(driver, MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait_for(driver, LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wait_for(driver, LoginPageLocators.ORDER_BUTTON)
        assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()

    def test_login_from_registration_page(self, driver, valid_user):
        driver.get(BASE_URL + "register")
        wait_for(driver, RegistrationPageLocators.LOGIN_BUTTON_ON_REG_FORM).click()
        wait_for(driver, LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wait_for(driver, LoginPageLocators.ORDER_BUTTON)
        assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()

    def test_login_from_password_recovery_page(self, driver, valid_user):
        driver.get(BASE_URL + "forgot-password")
        wait_for(driver, PasswordRecoveryPageLocators.LOGIN_BUTTON_ON_RECOVER_FORM).click()
        wait_for(driver, LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wait_for(driver, LoginPageLocators.ORDER_BUTTON)
        assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()