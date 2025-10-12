from pages.base_page import BasePage
from pages.locators import ProfilePageLocators


class ProfilePage(BasePage):
    def logout(self):
        self.click(self.driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON))
