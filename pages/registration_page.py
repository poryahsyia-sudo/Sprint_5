from .base_page import BasePage
from .locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def register(self, name, email, password):
        self.send_keys(RegistrationPageLocators.NAME_INPUT, name)
        self.send_keys(RegistrationPageLocators.EMAIL_INPUT, email)
        self.send_keys(RegistrationPageLocators.PASSWORD_INPUT, password)
        self.click(RegistrationPageLocators.REGISTER_BUTTON)
