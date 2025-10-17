import pytest
from selenium.webdriver.common.by import By
from data.urls import BASE_URL
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@pytest.mark.usefixtures("driver")
class TestRegistrationAndLogin:

    def test_successful_registration(self, driver, valid_user):
        """Проверка успешной регистрации"""
        page = RegistrationPage(driver)
        page.open(BASE_URL)
        page.register(valid_user["name"], valid_user["email"], valid_user["password"])
        assert driver.find_element(By.XPATH, "//p[contains(text(), 'Личный кабинет')]")

    def test_login_from_main_page(self, driver, valid_user):
        """Проверка входа через кнопку 'Войти в аккаунт' на главной странице"""
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        login_page = LoginPage(driver)
        login_page.login(valid_user["email"], valid_user["password"])
        assert driver.find_element(By.XPATH, "//p[contains(text(), 'Личный кабинет')]")

    def test_login_via_personal_account(self, driver, valid_user):
        """Проверка входа через кнопку 'Личный кабинет'"""
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        login_page = LoginPage(driver)
        login_page.login(valid_user["email"], valid_user["password"])
        assert driver.find_element(By.XPATH, "//p[contains(text(), 'Личный кабинет')]")

    def test_login_from_registration_page(self, driver, valid_user):
        """Проверка входа через ссылку 'Войти' со страницы регистрации"""
        driver.get(BASE_URL + "register")
        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        login_page = LoginPage(driver)
        login_page.login(valid_user["email"], valid_user["password"])
        assert driver.find_element(By.XPATH, "//p[contains(text(), 'Личный кабинет')]")

    def test_login_from_password_recovery_page(self, driver, valid_user):
        """Проверка входа через ссылку 'Войти' со страницы восстановления пароля"""
        driver.get(BASE_URL + "forgot-password")
        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        login_page = LoginPage(driver)
        login_page.login(valid_user["email"], valid_user["password"])
        assert driver.find_element(By.XPATH, "//p[contains(text(), 'Личный кабинет')]")
