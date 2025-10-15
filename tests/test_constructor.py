import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import BASE_URL
from pages.locators import ConstructorPageLocators, IngredientsLocators


@pytest.mark.usefixtures("driver")
class TestConstructorTabs:

    def open_page(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.BUNS_TAB)
        )

    def click_tab(self, driver, locator):
        tab = driver.find_element(*locator)
        driver.execute_script("arguments[0].scrollIntoView(true);", tab)
        driver.execute_script("arguments[0].click();", tab)

    def is_tab_active(self, driver, tab_locator):
        parent_div = driver.find_element(*tab_locator).find_element("xpath", "./parent::div")
        return "tab_tab_type_current" in parent_div.get_attribute("class")

    def test_fillings_tab(self, driver):
        self.open_page(driver)
        self.click_tab(driver, ConstructorPageLocators.FILLINGS_TAB)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(IngredientsLocators.FILLING_MEAT)
        )
        assert self.is_tab_active(driver, ConstructorPageLocators.FILLINGS_TAB)

    def test_sauces_tab(self, driver):
        self.open_page(driver)
        self.click_tab(driver, ConstructorPageLocators.SAUCES_TAB)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(IngredientsLocators.SAUCE_SPICY_X)
        )
        assert self.is_tab_active(driver, ConstructorPageLocators.SAUCES_TAB)

    def test_buns_tab(self, driver):
        self.open_page(driver)
        self.click_tab(driver, ConstructorPageLocators.BUNS_TAB)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(IngredientsLocators.BUN_R2D3)
        )
        assert self.is_tab_active(driver, ConstructorPageLocators.BUNS_TAB)
