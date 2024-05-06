from config import *
from locators import BurgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAccount:
    def test_navigate_from_main_to_personal_account_positive(self, driver):
        driver.get(MAIN_URL)
        driver.find_element(*BurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.LOGIN_FORM_HEADER))
        driver.find_element(*BurgersLocators.EMAIL_FIELD).send_keys('kristina@ya.ru')
        driver.find_element(*BurgersLocators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*BurgersLocators.LOGIN_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.CHECKOUT_BUTTON))
        driver.find_element(*BurgersLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.LOGIN_FIELD))

        assert driver.current_url == PERSONAL_ACCOUNT_URL, 'Не был выполнен переход на страницу ЛК'

    def test_navigate_from_personal_account_to_constructor_positive(self, driver):
        driver.get(MAIN_URL)
        driver.find_element(*BurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.LOGIN_FORM_HEADER))
        driver.find_element(*BurgersLocators.EMAIL_FIELD).send_keys('kristina@ya.ru')
        driver.find_element(*BurgersLocators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*BurgersLocators.LOGIN_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.CHECKOUT_BUTTON))
        driver.find_element(*BurgersLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.EXIT_BUTTON))
        driver.find_element(*BurgersLocators.CONSTRUCTOR_MENU_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.CONSTRUCTOR_HEADER))

        assert driver.current_url == f'{MAIN_URL}/', 'Не был выполнен переход на главную страницу'

    def test_logout_from_personal_account_positive(self, driver):
        driver.get(MAIN_URL)
        driver.find_element(*BurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.LOGIN_FORM_HEADER))
        driver.find_element(*BurgersLocators.EMAIL_FIELD).send_keys('kristina@ya.ru')
        driver.find_element(*BurgersLocators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*BurgersLocators.LOGIN_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.CHECKOUT_BUTTON))
        driver.find_element(*BurgersLocators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.EXIT_BUTTON))
        driver.find_element(*BurgersLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.LOGIN_FORM_HEADER))

        assert driver.current_url == LOGIN_URL, 'Не был выполнен переход на страницу логина'
