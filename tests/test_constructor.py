from config import *
from locators import BurgersLocators


class TestConstructor:
    def test_navigate_to_buns_positive(self, driver):
        driver.get(MAIN_URL)
        driver.find_element(*BurgersLocators.FILLINGS_CONSTRUCTOR_TAB).click()
        driver.find_element(*BurgersLocators.BUNS_CONSTRUCTOR_TAB).click()

        assert 'tab_tab_type_current' in driver.find_element(*BurgersLocators.BUNS_CONSTRUCTOR_TAB).get_attribute(
            'class'), 'Вкладка "Булки" не стала активной'

    def test_navigate_to_sauces_positive(self, driver):
        driver.get(MAIN_URL)
        driver.find_element(*BurgersLocators.SAUCES_CONSTRUCTOR_TAB).click()

        assert 'tab_tab_type_current' in driver.find_element(*BurgersLocators.SAUCES_CONSTRUCTOR_TAB).get_attribute(
                'class'), 'Вкладка "Соусы" не стала активной'

    def test_navigate_to_fillings_positive(self, driver):
        driver.get(MAIN_URL)
        driver.find_element(*BurgersLocators.FILLINGS_CONSTRUCTOR_TAB).click()

        assert 'tab_tab_type_current' in driver.find_element(*BurgersLocators.FILLINGS_CONSTRUCTOR_TAB).get_attribute(
            'class'), 'Вкладка "Начинки" не стала активной'
