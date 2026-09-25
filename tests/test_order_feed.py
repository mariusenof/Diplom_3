import allure

from pages.order_feed_page import OrderFeedPage
from urls import ORDER_FEED_URL


@allure.suite('Лента заказов')
class TestOrderFeed:

    @allure.title('При клике на заказ открывается модальное окно')
    def test_click_order_opens_modal(self, driver):
        page = OrderFeedPage(
            driver,
            ORDER_FEED_URL
        )
        page.open()

        page.click_first_order()

        assert page.is_order_modal_visible()

    @allure.title(
        'В ленте заказов отображается счётчик выполненных заказов за всё время'
    )
    def test_total_orders_counter_is_displayed(self, driver):
        page = OrderFeedPage(
            driver,
            ORDER_FEED_URL
        )
        page.open()

        total_counter = page.get_total_counter()

        assert total_counter.isdigit()

    @allure.title(
        'В ленте заказов отображается счётчик выполненных заказов за сегодня'
    )
    def test_today_orders_counter_is_displayed(self, driver):
        page = OrderFeedPage(
            driver,
            ORDER_FEED_URL
        )
        page.open()

        today_counter = page.get_today_counter()

        assert today_counter.isdigit()