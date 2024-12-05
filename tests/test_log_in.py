from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Constants
from conftest import driver
from locators import Locators


class TestLogIn:
    # тест 1 Вход по кнопке «Войти в аккаунт» на главной странице
    def test_log_in_by_enter_to_account_button(self, driver):
        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

        # поле ввода емейла
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_ENTER).send_keys(Constants.EMAIL)

        # поле ввода пароля
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ENTER).send_keys(Constants.PASSWORD)

        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_BUTTON).click()

        # кликнуть на кнопку личного кабинета
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()

        # подождать загрузку профиля
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_PAGE_HEADER))

        # проверить что логин корректный
        assert driver.find_element(*Locators.ACCOUNT_LOGIN_FIELD).get_attribute("value") == Constants.NAME

    # тест 2 вход через кнопку «Личный кабинет»
    def test_log_in_by_personal_account_button(self, driver):
        # кликнуть на кнопку личного кабинета
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()

        # подождать пока отрисуется форма входа
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ENTER_FORM_HEADER))

        # поле ввода емейла
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_ENTER).send_keys(Constants.EMAIL)

        # поле ввода пароля
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ENTER).send_keys(Constants.PASSWORD)

        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_BUTTON).click()

        # кликнуть на кнопку личного кабинета
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()

        # подождать загрузку профиля
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_PAGE_HEADER))

        # проверить что логин корректный
        assert driver.find_element(*Locators.ACCOUNT_LOGIN_FIELD).get_attribute("value") == Constants.NAME

    # тест 3 вход через кнопку в форме регистрации
    def test_log_in_by_registration_link(self, driver):
        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

        # подождать пока отрисуется форма входа
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ENTER_FORM_HEADER))

        # ссылка зарегистрироваться
        driver.find_element(*Locators.REGISTRATION_LINK).click()

        # подождать отрисовку формы регистрации
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_HEADER))

        # кликнуть ссылку "войти"
        driver.find_element(*Locators.ENTER_LINK).click()

        # подождать пока отрисуется форма входа
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ENTER_FORM_HEADER))

        # поле ввода емейла
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_ENTER).send_keys(Constants.EMAIL)

        # поле ввода пароля
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ENTER).send_keys(Constants.PASSWORD)

        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_BUTTON).click()

        # кликнуть на кнопку личного кабинета
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()

        # подождать загрузку профиля
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_PAGE_HEADER))

        # проверить что логин корректный
        assert driver.find_element(*Locators.ACCOUNT_LOGIN_FIELD).get_attribute("value") == Constants.NAME

    # тест 4 вход через кнопку в форме восстановления пароля
    def test_log_in_by_password_restore_link(self, driver):
        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

        # подождать пока отрисуется форма входа
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ENTER_FORM_HEADER))

        # кликнуть на ссылку 'восстановить пароль'
        driver.find_element(*Locators.RESTORE_PASSWORD_LINK).click()

        # подождать отрисовку формы восстановения пароля
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.RESTORE_PASSWORD_HEADER))

        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_LINK).click()

        # подождать пока отрисуется форма входа
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ENTER_FORM_HEADER))

        # поле ввода емейла
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_ENTER).send_keys(Constants.EMAIL)

        # поле ввода пароля
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_ENTER).send_keys(Constants.PASSWORD)

        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_BUTTON).click()

        # кликнуть на кнопку личного кабинета
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()

        # подождать загрузку профиля
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ACCOUNT_PAGE_HEADER))

        # проверить что логин корректный
        assert driver.find_element(*Locators.ACCOUNT_LOGIN_FIELD).get_attribute("value") == Constants.NAME
