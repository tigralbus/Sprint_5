from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Constants, Attributes
from conftest import driver
from locators import Locators


class TestConstructorTabs:
    # 1 тест проверка перехода к разделу «Соусы»
    def test_constructor_page_switch_to_sousi_tab(self, driver):
        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

        # поле ввода емейла
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_ENTER).send_keys(Constants.EMAIL)

        # поле ввода пароля
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(Constants.PASSWORD)

        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_BUTTON).click()

        # подождать пока появится хедер соберите бургер
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_HEADER))

        # кликнуть на табу Соусы
        driver.find_element(*Locators.SOUSI_TAB).click()

        # проверить что атрибут класс у "Соусы" изменился
        assert driver.find_element(*Locators.SOUSI_TAB).get_attribute(
            'class') == Attributes.TAB_SELECTED_CLASS and driver.find_element(*Locators.BULKI_TAB).get_attribute(
            'class') == Attributes.TAB_NOT_SELECTED_CLASS and driver.find_element(*Locators.NACHNKI_TAB).get_attribute(
            'class') == Attributes.TAB_NOT_SELECTED_CLASS

    # 2 тест Проверка перехода к разделу «Булки»
    def test_constructor_page_switch_to_bulki_tab(self, driver):
        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

        # поле ввода емейла
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_ENTER).send_keys(Constants.EMAIL)

        # поле ввода пароля
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(Constants.PASSWORD)

        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_BUTTON).click()

        # подождать пока появится хедер соберите бургер
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_HEADER))
        # кликнуть на табу "Соусы"
        driver.find_element(*Locators.SOUSI_TAB).click()

        # вернуться на табу "Булки"
        driver.find_element(*Locators.BULKI_TAB).click()

        # проверить что атрибут класс у "Соусы" изменился
        assert driver.find_element(*Locators.BULKI_TAB).get_attribute(
            'class') == Attributes.TAB_SELECTED_CLASS and driver.find_element(*Locators.SOUSI_TAB).get_attribute(
            'class') == Attributes.TAB_NOT_SELECTED_CLASS and driver.find_element(*Locators.NACHNKI_TAB).get_attribute(
            'class') == Attributes.TAB_NOT_SELECTED_CLASS

    # 3 тест Проверка перехода к разделу "Начинки"»"
    def test_constructor_page_switch_to_nachinki_tab(self, driver):
        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

        # поле ввода емейла
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_ENTER).send_keys(Constants.EMAIL)

        # поле ввода пароля
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(Constants.PASSWORD)

        # войти в аккаунт кнопка
        driver.find_element(*Locators.ENTER_BUTTON).click()

        # подождать пока появится хедер соберите бургер
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BURGER_CONSTRUCTOR_HEADER))
        # кликнуть на табу Начинки
        driver.find_element(*Locators.NACHNKI_TAB).click()

        # проверить что атрибут класс у "Соусы" изменился
        assert driver.find_element(*Locators.NACHNKI_TAB).get_attribute(
            'class') == Attributes.TAB_SELECTED_CLASS and driver.find_element(*Locators.SOUSI_TAB).get_attribute(
            'class') == Attributes.TAB_NOT_SELECTED_CLASS and driver.find_element(*Locators.BULKI_TAB).get_attribute(
            'class') == Attributes.TAB_NOT_SELECTED_CLASS
