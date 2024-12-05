from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Constants
from conftest import driver
from locators import Locators


class TestLogOut:
    # тест выход по кнопке «Выйти» в личном кабинете
    def test_log_in_by_enter_to_account_button(self, driver):
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

        # кликнуть на кнопку "Выход"
        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        # подождать пока отрисуется форма входа
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ENTER_FORM_HEADER))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
