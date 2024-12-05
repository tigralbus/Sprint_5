from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Constants
from conftest import driver
from locators import Locators


class TestGoToAccount:
    # тест проверка перехода по клику на кнопку «Личный кабинет».
    def test_switch_to_personal_account_page(self, driver):
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

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
