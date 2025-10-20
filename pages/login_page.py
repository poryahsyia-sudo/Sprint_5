from pages.locators import LoginPageLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def login(self, email, password):
        # вводим email и пароль и нажимаем кнопку входа
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).clear()
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).clear()
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

