from selenium.webdriver.common.by import By


class MainPageLocators:

    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        ".//p[text()='Личный Кабинет']"
    )

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        ".//p[text()='Конструктор']"
    )

    ORDER_FEED_BUTTON = (
        By.XPATH,
        ".//p[text()='Лента Заказов']"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        ".//button[text()='Войти в аккаунт']"
    )

    BUNS_SECTION = (
        By.XPATH,
        ".//span[text()='Булки']"
    )

    SAUCES_SECTION = (
        By.XPATH,
        ".//span[text()='Соусы']"
    )

    FILLINGS_SECTION = (
        By.XPATH,
        ".//span[text()='Начинки']"
    )

    FIRST_INGREDIENT = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]"
    )

    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//*[text()='Детали ингредиента']"
    )

    INGREDIENT_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close')]"
    )

    CONSTRUCTOR_DROP_ZONE = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket')]"
    )

    FIRST_INGREDIENT_COUNTER = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]"
        "//p[contains(@class, 'counter_counter__num')]"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Оформить заказ']"
    )

    CREATED_ORDER_NUMBER = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title')]"
    )


class OrderFeedPageLocators:

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        ".//p[text()='Конструктор']"
    )

    FIRST_ORDER_CARD = (
        By.XPATH,
        "(//li[contains(@class, 'OrderHistory_listItem')]//a)[1]"
    )

    ORDER_MODAL = (
        By.XPATH,
        "//*[contains(text(), 'Cостав') or contains(text(), 'Состав')]"
    )

    TOTAL_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p"
    )

    TODAY_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )

    ORDERS_IN_PROGRESS_TITLE = (
        By.XPATH,
        "//*[text()='В работе:']"
    )


class LoginPageLocators:

    EMAIL_INPUT = (
        By.XPATH,
        "//input[@type='text']"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password']"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )

    MODAL_OVERLAY = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal_overlay')]"
    )