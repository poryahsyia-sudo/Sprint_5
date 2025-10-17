import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import BASE_URL
from pages.locators import ConstructorPageLocators, IngredientsLocators


@pytest.mark.usefixtures("driver")
class TestConstructorTabs:

    def test_fillings_tab(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.BUNS_TAB)
        )
        # Переход на вкладку "Начинки"
        fillings_tab = driver.find_element(*ConstructorPageLocators.FILLINGS_TAB)
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings_tab)
        driver.execute_script("arguments[0].click();", fillings_tab)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(IngredientsLocators.FILLING_MEAT)
        )
        # Проверяем, что вкладка активна
        parent_div = driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).find_element("xpath", "./parent::div")
        assert "tab_tab_type_current" in parent_div.get_attribute("class")

    def test_sauces_tab(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.BUNS_TAB)
        )
        # Переход на вкладку "Начинки", чтобы уйти с "Булок"
        driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()
        # Переход на вкладку "Соусы"
        sauces_tab = driver.find_element(*ConstructorPageLocators.SAUCES_TAB)
        driver.execute_script("arguments[0].scrollIntoView(true);", sauces_tab)
        driver.execute_script("arguments[0].click();", sauces_tab)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(IngredientsLocators.SAUCE_SPICY_X)
        )
        parent_div = driver.find_element(*ConstructorPageLocators.SAUCES_TAB).find_element("xpath", "./parent::div")
        assert "tab_tab_type_current" in parent_div.get_attribute("class")

    def test_buns_tab(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.BUNS_TAB)
        )
        # Уходим с вкладки "Булки"
        driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
        # Возвращаемся на вкладку "Булки"
        buns_tab = driver.find_element(*ConstructorPageLocators.BUNS_TAB)
        driver.execute_script("arguments[0].scrollIntoView(true);", buns_tab)
        driver.execute_script("arguments[0].click();", buns_tab)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(IngredientsLocators.BUN_R2D3)
        )
        parent_div = driver.find_element(*ConstructorPageLocators.BUNS_TAB).find_element("xpath", "./parent::div")
        assert "tab_tab_type_current" in parent_div.get_attribute("class")