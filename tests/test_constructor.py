import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ConstructorPageLocators, IngredientsLocators
from data.urls import BASE_URL  # ✅ возвращено как у тебя


@pytest.mark.parametrize("tab_locator,ingredient_locator", [
    (ConstructorPageLocators.FILLINGS_TAB, IngredientsLocators.FILLING_MEAT),
    (ConstructorPageLocators.SAUCES_TAB, IngredientsLocators.SAUCE_SPICY_X),
    (ConstructorPageLocators.BUNS_TAB, IngredientsLocators.BUN_R2D3),
])
def test_tabs_navigation(driver, tab_locator, ingredient_locator):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    # 🔹 Ожидаем, что вкладка кликабельна
    tab = wait.until(EC.element_to_be_clickable(tab_locator))
    tab.click()

    # 🔹 Ждём, пока вкладка станет активной
    wait.until(lambda d: "tab_tab_type_current" in tab.get_attribute("class"))

    # 🔹 Проверяем, что появился ингредиент
    wait.until(EC.visibility_of_element_located(ingredient_locator))
    assert driver.find_element(*ingredient_locator).is_displayed()