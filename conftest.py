import random
import pytest
from selenium import webdriver

@pytest.fixture #фикстура, которая инициализирует драйвер
def driver():
    browser = webdriver.Chrome()
    browser.get("https://stellarburgers.nomoreparties.site/")
    return browser
    #yield browser
    #browser.quit()

@pytest.fixture #фикстура, которая создаёт name
def name_generator():
    name = 'Эдмандрууил ' + str(random.randint(10, 9999999))
    return name

@pytest.fixture #фикстура, которая возвращает реальное имя юзера
def get_user_name():
    return 'Anastasia'

@pytest.fixture #фикстура, которая возвращает реальный email
def get_user_email():
    return 'anastasia_dotsina_16_158@ya.ru'

@pytest.fixture #фикстура, которая создаёт email
def email_generator():
    email = str(random.randint(100, 999)) + '@ya.ru'
    return email

@pytest.fixture #фикстура, которая создаёт  password
def password_generator():
    password = str(random.randint(100000, 999999))
    return password

@pytest.fixture #фикстура, которая создаёт  short password
def short_password_generator():
    password = str(random.randint(1000, 9999))
    return password

@pytest.fixture #фикстура, которая возвращает реальный password
def get_user_password():
    return '123456'