import allure

from pages.main_page import MainPage
from urls import MAIN_URL, LOGIN_URL, ORDER_FEED_URL


@allure.suite('Навигация')
class TestNavigation:

    @allure.title('Переход в личный кабинет')
    def test_go_to_personal_account(self, driver):
        page = MainPage(driver, MAIN_URL)
        page.open()

        page.click_personal_account()

        page.wait_for_url(LOGIN_URL)

        assert page.current_url() == LOGIN_URL

    @allure.title('Переход в ленту заказов')
    def test_go_to_order_feed(self, driver):
        page = MainPage(driver, MAIN_URL)
        page.open()

        page.click_order_feed()

        page.wait_for_url(ORDER_FEED_URL)

        assert page.current_url() == ORDER_FEED_URL