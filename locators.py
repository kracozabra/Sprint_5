from selenium.webdriver.common.by import By


class BurgersLocators:
    NAME_FIELD = (By.XPATH, './/label[text() = "Имя"]/../input')                   # Поле "Имя" на форме регистрации
    EMAIL_FIELD = (By.XPATH, './/label[text() = "Email"]/../input')                # Поле "Email" на форме регистрации
    PASSWORD_FIELD = (By.XPATH, './/label[text() = "Пароль"]/../input')            # Поле "Пароль" на форме регистрации
    LOGIN_FIELD = (By.XPATH, './/label[text() = "Логин"]/../input')                # Поле "Логин" на форме ЛК
    REG_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')              # Кнопка "Зарегистрироваться"
    REG_PASSWORD_VALIDATION = (By.XPATH, './/label[text() = "Пароль"]/../../p[contains(@class, "input__error")]')   #Сообщение валидации при вводе некорректного пароля
    LOGIN_FORM_HEADER = (By.XPATH, './/h2[text()="Вход"]')                         # Заголовок "Вход" на форме авторизации
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')               # Кнопка "Войти" на главной странице
    LOGIN_LINK = (By.LINK_TEXT, "Войти")                                           # Ссылка "Войти"
    LOGIN_FORM_BUTTON = (By.XPATH, './/button[text()="Войти"]')                    # Кнопка "Войти" на форме авторизации
    PERSONAL_ACCOUNT_LINK = (By.XPATH, './/header//p[text()="Личный Кабинет"]')    # Ссылка на личный кабинет
    CHECKOUT_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')             # Кнопка "Оформить заказ"
    CONSTRUCTOR_MENU_LINK = (By.XPATH, './/header//p[text()="Конструктор"]')       # Кнопка меню "Конструктор"
    CONSTRUCTOR_HEADER = (By.XPATH, './/h1[text()="Соберите бургер"]')             # Заголовок "Соберите бургер" на главной
    EXIT_BUTTON = (By.XPATH, './/button[text()="Выход"]')                          # Кнопка выхода из ЛК
    BUNS_CONSTRUCTOR_TAB = (By.XPATH, './/span[text()="Булки"]/..')                # Вкладка "Булки"
    SAUCES_CONSTRUCTOR_TAB = (By.XPATH, './/span[text()="Соусы"]/..')              # Вкладка "Соусы"
    FILLINGS_CONSTRUCTOR_TAB = (By.XPATH, './/span[text()="Начинки"]/..')          # Вкладка "Начинки"
    BUNS_CONSTRUCTOR_HEADER = (By.XPATH, './/h2[text()="Булки"]')                  # Заголовок "Булки"
    SAUCES_CONSTRUCTOR_HEADER = (By.XPATH, './/h2[text()="Соусы"]')                # Заголовок "Соусы"
    FILLINGS_CONSTRUCTOR_HEADER = (By.XPATH, './/h2[text()="Начинки"]')            # Заголовок "Начинки"
