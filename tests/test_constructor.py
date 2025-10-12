import time
import pytest
from pages.locators import ConstructorPageLocators, IngredientsLocators

def test_tabs_navigation(driver):
    # 1. Открываем главную страницу
    driver.get("https://stellarburgers.education-services.ru/")
    time.sleep(2)

    # 2. Переход на вкладку "Начинки" и проверка
    driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()
    time.sleep(1)
    assert driver.find_element(*IngredientsLocators.FILLING_MEAT).is_displayed()

    # 3. Переход на вкладку "Соусы" и проверка
    driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
    time.sleep(1)
    assert driver.find_element(*IngredientsLocators.SAUCE_SPICY_X).is_displayed()

    # 4. Переход на вкладку "Булки" и проверка
    driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()
    time.sleep(1)
    assert driver.find_element(*IngredientsLocators.BUN_R2D3).is_displayed()
