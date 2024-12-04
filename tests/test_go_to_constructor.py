from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from conftest import get_user_email, get_user_password, get_user_name, driver
from locators import Locators

class TestGoToConstructor:
    # 1 тест проверка перехода по клику на «Конструктор».
    def test_switch_to_constructor_page_by_constructor_button(self, get_user_email, get_user_password, get_user_name, driver):
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

        # кликнуть на кнопку "конструктор"
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        #подождать пока появится хедер соберите бургер
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_HEADER))

        assert driver.find_element(*Locators.BURGER_CONSTRUCTOR_HEADER).text == 'Соберите бургер'
        driver.quit()

    # 2 тест проверка перехода по клику на логотип Stellar Burgers.
    def test_switch_to_constructor_page_by_logo(self, get_user_email, get_user_password, get_user_name, driver):
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
        # кликнуть на логотип
        driver.find_element(*Locators.CONSTRUCTOR_LOGO).click()

        #подождать пока появится хедер соберите бургер
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_HEADER))

        assert driver.find_element(*Locators.BURGER_CONSTRUCTOR_HEADER).text == 'Соберите бургер'
        driver.quit()
