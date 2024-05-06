import pytest
from config import *
from locators import BurgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    @pytest.mark.parametrize(
        'start_url,button_locator',
        [
            [MAIN_URL, BurgersLocators.LOGIN_BUTTON],            #Вход по кнопке «Войти в аккаунт» на главной
            [MAIN_URL, BurgersLocators.PERSONAL_ACCOUNT_LINK],   #Вход через кнопку «Личный кабинет»
            [REG_URL, BurgersLocators.LOGIN_LINK],               #Вход через кнопку на форме регистрации
            [FORGOT_PASSWORD_URL, BurgersLocators.LOGIN_LINK]    #Вход через кнопку на форме восстановления пароля
        ]
    )
    def test_login_positive(self, driver, start_url, button_locator):
        driver.get(start_url)
        driver.find_element(*button_locator).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.LOGIN_FORM_HEADER))
        test_login = 'kristina@ya.ru'
        test_password = '123456'
        driver.find_element(*BurgersLocators.EMAIL_FIELD).send_keys(test_login)
        driver.find_element(*BurgersLocators.PASSWORD_FIELD).send_keys(test_password)
        driver.find_element(*BurgersLocators.LOGIN_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.CHECKOUT_BUTTON))
        driver.find_element(*BurgersLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.LOGIN_FIELD))
        current_login = driver.find_element(*BurgersLocators.LOGIN_FIELD).get_attribute('value')

        assert current_login == test_login, 'В личном профиле указан не тот Email, под которым проводилась авторизация'
