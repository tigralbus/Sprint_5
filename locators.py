from selenium.webdriver.common.by import By


class Locators:
    # Кнопка "Войти"
    ENTER_ACCOUNT_BUTTON = (
        By.XPATH,
        ".//section[@class = 'BurgerConstructor_basket__29Cd7 mt-25 ']/div/button[text() = 'Войти в аккаунт']")
    # Заголовок формы "Вход"
    ENTER_FORM_HEADER = (By.XPATH, ".//h2[text()='Вход']")
    # Поле ввода емейла формы Ввод
    EMAIL_INPUT_FIELD_ENTER = (By.XPATH, "*//input[@name = 'name']")
    # Поле ввода пароля формы Ввод
    PASSWORD_INPUT_FIELD = (By.XPATH, ".//input[@name='Пароль']")

    # Кнопка регистрации
    REGISTRATION_BUTTON = (By.XPATH,
                           ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    # Заголовок формы регистрации
    REGISTRATION_HEADER = (By.XPATH, ".//h2[text() = 'Регистрация']")
    # Ссылка на форму регистрации
    REGISTRATION_LINK = (By.XPATH, ".//div[@id='root']//a[@href='/register']")
    # Поле ввода имени формы Регистрация
    NAME_INPUT_FIELD_REG = (By.XPATH, ".//fieldset//label[text()='Имя']/../input")
    # Поле ввода емейла формы Регистрация
    EMAIL_INPUT_FIELD_REG = (By.XPATH, ".//fieldset//label[text()='Email']/../input")
    # Текст ошибки поля пароля
    PASSWORD_INPUT_FIELD_ERROR = (By.XPATH, ".//fieldset//p[@class = 'input__error text_type_main-default']")

    # Ссылка "Войти"
    ENTER_LINK = (By.CSS_SELECTOR, "a[class='Auth_link__1fOlj'][href='/login'")
    # Кнопка "Войти"
    ENTER_BUTTON = (By.CSS_SELECTOR,
                    "button[class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

    # Кнопка "Вход в личный кабинет"
    ACCOUNT_PAGE_BUTTON = (By.XPATH, ".//header/nav/a[@class='AppHeader_header__link__3D_hX']")
    # Заголовок страницы личного кабинета
    ACCOUNT_PAGE_HEADER = (By.CSS_SELECTOR,
                           "a[class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']")
    # Поле логина в Личном кабинете
    ACCOUNT_LOGIN_FIELD = (By.CSS_SELECTOR,
                           "input[class='text input__textfield text_type_main-default input__textfield-disabled'][name='Name']")
    # Заголовок формы восстановления пароля
    RESTORE_PASSWORD_HEADER = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")
    # Ссылка на форму восстановления пароля
    RESTORE_PASSWORD_LINK = (By.CSS_SELECTOR, "a[class='Auth_link__1fOlj'][href='/forgot-password']")

    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")

    # Заголовок страницы конструктора
    BURGER_CONSTRUCTOR_HEADER = (By.CSS_SELECTOR, "h1[class='text text_type_main-large mb-5 mt-10']")
    # Кнопка перехода в конструктор
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "a[class='AppHeader_header__link__3D_hX'][href='/']")
    # Лого конструктора
    CONSTRUCTOR_LOGO = (By.CSS_SELECTOR, "div[class = 'AppHeader_header__logo__2D0X2']")

    # Таба "Соусы"
    SOUSI_TAB = (By.XPATH, ".//main/section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Соусы']/..")
    # Таба "Булки"
    BULKI_TAB = (By.XPATH, ".//main/section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Булки']/..")
    # Таба "Начинки"
    NACHNKI_TAB = (
        By.XPATH, ".//main/section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Начинки']/..")
