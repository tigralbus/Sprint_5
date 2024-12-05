from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Messages
from locators import Locators
from conftest import name_generator, email_generator, password_generator, short_password_generator, driver


class TestRegistration:
    # 1 тест проверить успешную регистрацию. Поле «Имя» должно быть не пустым.
    def test_registration_completed(self, name_generator, email_generator, password_generator, driver):
        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

        # подождать пока отрисуется форма входа
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ENTER_FORM_HEADER))

        # ссылка зарегистрироваться
        driver.find_element(*Locators.REGISTRATION_LINK).click()

        # поле ввода имени
        driver.find_element(*Locators.NAME_INPUT_FIELD_REG).send_keys(name_generator)

        # поле ввода емейла
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_REG).send_keys(email_generator)

        # поле ввода пароля
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password_generator)

        # кнопка зарегистрироваться
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # форма логина загрузилась
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ENTER_FORM_HEADER))

        # поле ввода емейла
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_ENTER).send_keys(email_generator)

        # поле ввода пароля
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(password_generator)

        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_BUTTON).click()

        # кликнуть на кнопку личного кабинета
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()

        # подождать загрузку профиля
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_PAGE_HEADER))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    # 2 тест проверить появление ошибки при некорректном пароле
    def test_registration_short_password(self, name_generator, email_generator, short_password_generator, driver):
        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

        # подождать пока отрисуется форма входа
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ENTER_FORM_HEADER))

        # ссылка зарегистрироваться
        driver.find_element(*Locators.REGISTRATION_LINK).click()

        # поле ввода имени
        driver.find_element(*Locators.NAME_INPUT_FIELD_REG).send_keys(name_generator)

        # поле ввода емейла
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_REG).send_keys(email_generator)

        # поле ввода пароля
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(short_password_generator)

        # кнопка зарегистрироваться
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        assert driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ERROR).text == Messages.INCORRECT_PASSWORD_TEXT
