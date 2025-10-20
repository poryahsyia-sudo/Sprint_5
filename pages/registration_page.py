from pages.locators import RegistrationPageLocators

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def register(self, name, email, password):
        name_el = self.driver.find_element(*RegistrationPageLocators.NAME_FIELD)
        name_el.clear()
        name_el.send_keys(name)

        email_el = self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD)
        email_el.clear()
        email_el.send_keys(email)

        password_el = self.driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD)
        password_el.clear()
        password_el.send_keys(password)

        self.driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
