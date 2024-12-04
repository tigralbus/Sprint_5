from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from conftest import get_user_email, get_user_password, get_user_name, driver
from locators import Locators

class TestGoToAccount:
    # тест проверка перехода по клику на кнопку «Личный кабинет».
    def test_switch_to_personal_account_page(self, get_user_email, get_user_password, get_user_name,  driver):
        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

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

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        driver.quit()