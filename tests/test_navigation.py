import time
import pytest
from pages.locators import (
    MainPageLocators,
    LoginPageLocators,
    AccountPageLocators,
    ConstructorPageLocators,
)
from utils.generator import generate_email, generate_password

def test_login_and_go_to_account(driver, valid_user):
    # Открываем главную страницу
    driver.get("https://stellarburgers.education-services.ru/")
    time.sleep(1)

    # Нажимаем кнопку "Личный кабинет"
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    time.sleep(1)

    # Вводим email и пароль
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])

    # Нажимаем кнопку "Войти"
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)

    # Нажимаем снова "Личный кабинет" (переход в профиль)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    time.sleep(2)

    # Проверяем, что видна кнопка "Профиль" в ЛК (переход успешен)
    profile_button = driver.find_element(*AccountPageLocators.PROFILE_BUTTON)
    assert profile_button.is_displayed()

def test_login_and_go_to_constructor(driver, valid_user):
    # 1. Открываем главную страницу
    driver.get("https://stellarburgers.education-services.ru/")
    time.sleep(1)

    # 2. Нажимаем кнопку "Войти в аккаунт"
    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
    time.sleep(1)

    # Вводим данные пользователя и входим
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)

    # 3. Переход в личный кабинет
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    time.sleep(2)
    assert driver.find_element(*AccountPageLocators.PROFILE_BUTTON).is_displayed()

    # 4. Переход в Конструктор через кнопку
    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
    time.sleep(2)

    # 5. Проверка, что кнопка "Оформить заказ" видна на странице конструктора
    assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()

def test_login_and_go_to_home_via_stellar_logo(driver, valid_user):
    # 1. Открываем главную страницу
    driver.get("https://stellarburgers.education-services.ru/")
    time.sleep(1)

    # 2. Входим через "Войти в аккаунт"
    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)

    # 3. Переходим в Личный кабинет
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    time.sleep(2)
    assert driver.find_element(*AccountPageLocators.PROFILE_BUTTON).is_displayed()

    # 4. Кликаем по логотипу Stellar Burgers — должен перейти на главную
    driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
    time.sleep(2)

    # 5. Проверяем, что кнопка "Оформить заказ" видна на главной
    assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()

def test_logout_from_account(driver, valid_user):
    # 1. Открываем главную страницу и входим
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(valid_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(valid_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)

    # 2. Переходим в Личный кабинет
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    time.sleep(2)
    assert driver.find_element(*AccountPageLocators.PROFILE_BUTTON).is_displayed()

    # 3. Нажимаем кнопку "Выйти"
    driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).click()
    time.sleep(2)

    # 4. Проверяем, что произошёл редирект на страницу логина
    assert "login" in driver.current_url
