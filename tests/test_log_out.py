from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from conftest import get_user_email, get_user_password, get_user_name, get_user_name, driver
from locators import Locators

class TestLogOut:
    # тест выход по кнопке «Выйти» в личном кабинете
    def test_log_in_by_enter_to_account_button(self,get_user_email, get_user_password, get_user_name, driver):
        # кликнуть на кнопку личного кабинета
        driver.find_element(*Locators.ACCOUNT_PAGE_BUTTON).click()

        # подождать пока отрисуется форма входа
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ENTER_FORM_HEADER))

        # поле ввода емейла
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(get_user_email)

        # поле ввода пароля
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(get_user_password)

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

        driver.quit()