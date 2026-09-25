import time

from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators import MainPageLocators


class OrderFeedPage(BasePage):

    def click_first_order(self):
        self.click_element_js(
            MainPageLocators.FIRST_ORDER_CARD
        )

    def is_order_modal_visible(self):
        return self.find_element(
            MainPageLocators.ORDER_MODAL
        ).is_displayed()

    def get_total_counter(self):
        return self.get_text(
            MainPageLocators.TOTAL_COUNTER
        )

    def get_today_counter(self):
        return self.get_text(
            MainPageLocators.TODAY_COUNTER
        )

    def is_order_number_in_progress(self, order_number):
        self.find_element(
            MainPageLocators.ORDERS_IN_PROGRESS_TITLE
        )

        order_locator = (
            'xpath',
            f"//*[normalize-space()='{order_number}']"
        )

        for _ in range(10):
            try:
                element = self.find_element(
                    order_locator,
                    timeout=2
                )

                if element.is_displayed():
                    return True

            except TimeoutException:
                pass

            self.driver.refresh()
            time.sleep(1)

        return False