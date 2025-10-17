from pages.locators import ProfilePageLocators

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

