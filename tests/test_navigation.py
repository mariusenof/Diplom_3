import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from urls import MAIN_URL, ORDER_FEED_URL


@allure.suite('Навигация')
class TestNavigation:

    @allure.title(
        'Переход из конструктора в ленту заказов'
    )
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(
            driver,
            MAIN_URL
        )

        main_page.open()

        main_page.click_order_feed()

        main_page.wait_for_url(
            ORDER_FEED_URL
        )

        assert (
            main_page.current_url().rstrip('/')
            == ORDER_FEED_URL.rstrip('/')
        )

    @allure.title(
        'Переход из ленты заказов в конструктор'
    )
    def test_go_to_constructor(self, driver):
        order_feed_page = OrderFeedPage(
            driver,
            ORDER_FEED_URL
        )

        order_feed_page.open()

        order_feed_page.click_constructor()

        order_feed_page.wait_for_url(
            MAIN_URL
        )

        assert (
            order_feed_page.current_url().rstrip('/')
            == MAIN_URL.rstrip('/')
        )