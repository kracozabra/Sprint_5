import random
import pytest
from config import *
from locators import BurgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    def test_registration_correct_data_positive(self, driver):
        driver.get(REG_URL)
        driver.find_element(*BurgersLocators.NAME_FIELD).send_keys('Кристина')
        driver.find_element(*BurgersLocators.EMAIL_FIELD).send_keys(f'Kristina{random.randint(1, 1000)}@ya.ru')
        driver.find_element(*BurgersLocators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*BurgersLocators.REG_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.LOGIN_FORM_HEADER))

        assert driver.current_url == LOGIN_URL, 'Не произошел переход на страницу логина'

    @pytest.mark.parametrize('password', ['1', '12345'])
    def test_registration_short_password_negative(self, driver, password):
        driver.get(REG_URL)
        driver.find_element(*BurgersLocators.NAME_FIELD).send_keys('Кристина')
        driver.find_element(*BurgersLocators.EMAIL_FIELD).send_keys(f'kristina{random.randint(1, 1000)}@ya.ru')
        driver.find_element(*BurgersLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*BurgersLocators.REG_BUTTON).click()

        assert driver.find_element(*BurgersLocators.REG_PASSWORD_VALIDATION).text == 'Некорректный пароль', 'Не появилось сообщение "Некорректный пароль"'
