import time
import pytest
from utils.generator import generate_email, generate_password
from pages.locators import (
    MainPageLocators,
    RegistrationPageLocators,
    LoginPageLocators,
    PasswordRecoveryPageLocators,
)

def test_successful_registration(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    # Переход на страницу регистрации
    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element("link text", "Зарегистрироваться").click()

    # Заполнение формы
    email = generate_email()
    password = generate_password()
    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Test User")
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)

    # Отправка формы
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    time.sleep(3)

    # Вход с только что зарегистрированным пользователем
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(3)

    # Проверка успешного входа по кнопке "Оформить заказ"
    assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()
    

def test_login_from_main_page(driver, valid_user):
    driver.get("https://stellarburgers.education-services.ru/")
    time.sleep(1)

    # Нажимаем кнопку "Войти в аккаунт"
    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
    time.sleep(1)

    # Вводим Email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])

    # Нажимаем кнопку "Войти"
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)

    # Проверка успешного входа через наличие кнопки "Оформить заказ"
    assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()

def test_login_via_personal_account(driver, valid_user):
    driver.get("https://stellarburgers.education-services.ru/")
    time.sleep(1)

    # Нажимаем кнопку "Личный кабинет"
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    time.sleep(1)

    # Проверяем, что форма Email/Пароль отображается
    assert driver.find_element(*LoginPageLocators.EMAIL_FIELD).is_displayed()
    assert driver.find_element(*LoginPageLocators.PASSWORD_FIELD).is_displayed()
    assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()

    # Вводим данные и входим
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)

    # Проверяем успешный вход
    assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()

def test_login_from_registration_page(driver, valid_user):
    driver.get("https://stellarburgers.education-services.ru/register")
    time.sleep(1)

    # Нажимаем кнопку "Войти" на форме регистрации
    driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON_ON_REG_FORM).click()
    time.sleep(1)

    # Вводим email и пароль валидного пользователя и входим
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)

    assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()

def test_login_from_password_recovery_page(driver, valid_user):
    driver.get("https://stellarburgers.education-services.ru/forgot-password")
    time.sleep(1)

    # Нажимаем кнопку "Войти" на форме восстановления
    driver.find_element(*PasswordRecoveryPageLocators.LOGIN_BUTTON_ON_RECOVER_FORM).click()
    time.sleep(1)

    # Вводим данные и входим
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)

    assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()
