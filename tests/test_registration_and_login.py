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


def test_successful_registration(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element("link text", "Зарегистрироваться").click()
    email = generate_email()
    password = generate_password()
    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Test User")
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
    )
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON)
    )
    assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()
