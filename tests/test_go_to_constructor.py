from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Constants
from conftest import driver
from locators import Locators


class TestGoToConstructor:
    # 1 тест проверка перехода по клику на «Конструктор».
    def test_switch_to_constructor_page_by_constructor_button(self, driver):
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

        # кликнуть на кнопку "конструктор"
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        # подождать пока появится хедер соберите бургер
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_HEADER))

        assert driver.find_element(*Locators.BURGER_CONSTRUCTOR_HEADER).text == 'Соберите бургер'

    # 2 тест проверка перехода по клику на логотип Stellar Burgers.
    def test_switch_to_constructor_page_by_logo(self, driver):
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
        # кликнуть на логотип
        driver.find_element(*Locators.CONSTRUCTOR_LOGO).click()

        # подождать пока появится хедер соберите бургер
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_HEADER))

        assert driver.find_element(*Locators.BURGER_CONSTRUCTOR_HEADER).text == 'Соберите бургер'
