from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка ЛК
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка Конструктор
    LOGO_BUTTON = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип
    PASSWORD_RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # Кнопка "Восстановить" в форме восстановления пароля


class RegistrationPageLocators:
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")  # Поле имя
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # Поле email
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле пароль
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]")  # Ошибка под полем
    LOGIN_BUTTON_ON_REG_FORM = (By.XPATH, ".//a[text()='Войти']")  # Кнопка "Войти" на форме регистрации


class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выйти" в личном кабинете


class ConstructorPageLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # Вкладка "Булки"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # Вкладка "Соусы"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # Вкладка "Начинки"
    ACTIVE_SECTION_TITLE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span")  # Активная вкладка


class IngredientsLocators:
    BUN_R2D3 = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a")
    SAUCE_SPICY_X = (By.XPATH, "//p[text()='Соус Spicy-X']")
    FILLING_MEAT = (By.XPATH, "//p[text()='Мясная начинка']/ancestor::a")


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка входа
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"


class AccountPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PROFILE_BUTTON = (By.XPATH, "//a[contains(text(), 'Профиль')]")

class PasswordRecoveryPageLocators:
    LOGIN_BUTTON_ON_RECOVER_FORM = (By.XPATH, ".//a[text()='Войти']")  # Кнопка "Войти" на форме восстановления пароля
