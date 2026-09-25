import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from urls import LOGIN_URL, MAIN_URL, ORDER_FEED_URL


@allure.suite('Лента заказов')
class TestCreatedOrderInFeed:

    @allure.title(
        'Созданный заказ появляется в разделе "В работе" ленты заказов'
    )
    def test_created_order_number_appears_in_progress(
        self,
        driver,
        user
    ):
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

        order_number = main_page.get_created_order_number()

        order_feed_page = OrderFeedPage(
            driver,
            ORDER_FEED_URL
        )

        order_feed_page.open()

        assert order_feed_page.is_order_number_in_progress(
            order_number
        )