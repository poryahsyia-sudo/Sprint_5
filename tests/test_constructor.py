import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ConstructorPageLocators, IngredientsLocators
from data.urls import BASE_URL  # ✅ возвращено как у тебя

def test_fillings_tab(driver):
    driver.get(BASE_URL)
    driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(IngredientsLocators.FILLING_MEAT)
    )
    fillings_tab = driver.find_element(*ConstructorPageLocators.FILLINGS_TAB)
    assert "tab_tab_type_current" in fillings_tab.get_attribute("class")


def test_sauces_tab(driver):
    driver.get(BASE_URL)
    driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(IngredientsLocators.SAUCE_SPICY_X)
    )
    sauces_tab = driver.find_element(*ConstructorPageLocators.SAUCES_TAB)
    assert "tab_tab_type_current" in sauces_tab.get_attribute("class")


def test_buns_tab(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(ConstructorPageLocators.BUNS_TAB)
    ).click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(IngredientsLocators.BUN_R2D3)
    )
    buns_tab = driver.find_element(*ConstructorPageLocators.BUNS_TAB)
    assert "tab_tab_type_current" in buns_tab.get_attribute("class")