from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def login(self, email, password):
        self.send_keys(self.driver.find_element(*LoginPageLocators.EMAIL_FIELD), email)
        self.send_keys(self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD), password)
        self.click(self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON))
