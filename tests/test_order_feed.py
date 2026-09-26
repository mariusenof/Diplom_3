import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from urls import LOGIN_URL, MAIN_URL, ORDER_FEED_URL


@allure.suite('Лента заказов')
class TestOrderFeed:

    @allure.title(
        'При клике на заказ открывается модальное окно'
    )
    def test_click_order_opens_modal(
        self,
        driver
    ):
        order_feed_page = OrderFeedPage(
            driver,
            ORDER_FEED_URL
        )

        order_feed_page.open()

        order_feed_page.click_first_order()

        assert order_feed_page.is_order_modal_visible()

    @allure.title(
        'После создания заказа счётчик '
        '"Выполнено за всё время" увеличивается'
    )
    def test_total_orders_counter_increases_after_order_creation(
        self,
        driver,
        user
    ):
        order_feed_page = OrderFeedPage(
            driver,
            ORDER_FEED_URL
        )

        order_feed_page.open()

        counter_before = (
            order_feed_page.get_total_counter()
        )

        login_page = LoginPage(
            driver,
            LOGIN_URL
        )

        login_page.open()

        login_page.login(
            user['email'],
            user['password']
        )

        main_page = MainPage(
            driver,
            MAIN_URL
        )

        main_page.wait_for_url(
            MAIN_URL
        )

        main_page.drag_first_ingredient_to_constructor()

        main_page.click_order_button()

        main_page.get_created_order_number()

        order_feed_page.open()

        assert (
            order_feed_page.wait_total_counter_increased(
                counter_before
            )
        )

    @allure.title(
        'После создания заказа счётчик '
        '"Выполнено за сегодня" увеличивается'
    )
    def test_today_orders_counter_increases_after_order_creation(
        self,
        driver,
        user
    ):
        order_feed_page = OrderFeedPage(
            driver,
            ORDER_FEED_URL
        )

        order_feed_page.open()

        counter_before = (
            order_feed_page.get_today_counter()
        )

        login_page = LoginPage(
            driver,
            LOGIN_URL
        )

        login_page.open()

        login_page.login(
            user['email'],
            user['password']
        )

        main_page = MainPage(
            driver,
            MAIN_URL
        )

        main_page.wait_for_url(
            MAIN_URL
        )

        main_page.drag_first_ingredient_to_constructor()

        main_page.click_order_button()

        main_page.get_created_order_number()

        order_feed_page.open()

        assert (
            order_feed_page.wait_today_counter_increased(
                counter_before
            )
        )