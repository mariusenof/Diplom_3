from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    def click_constructor(self):
        self.wait_for_element_invisible(
            OrderFeedPageLocators.MODAL_OVERLAY
        )

        self.click_element_js(
            OrderFeedPageLocators.CONSTRUCTOR_BUTTON
        )

    def click_first_order(self):
        self.click_element_js(
            OrderFeedPageLocators.FIRST_ORDER_CARD
        )

    def is_order_modal_visible(self):
        return self.find_element(
            OrderFeedPageLocators.ORDER_MODAL
        ).is_displayed()

    def get_total_counter(self):
        text = self.get_text(
            OrderFeedPageLocators.TOTAL_COUNTER
        )

        return int(
            text.replace(' ', '')
        )

    def get_today_counter(self):
        text = self.get_text(
            OrderFeedPageLocators.TODAY_COUNTER
        )

        return int(
            text.replace(' ', '')
        )

    def wait_total_counter_increased(
        self,
        previous_value,
        timeout=30
    ):
        return self.wait_for_condition_with_refresh(
            lambda driver:
            self.get_total_counter() > previous_value,
            timeout=timeout
        )

    def wait_today_counter_increased(
        self,
        previous_value,
        timeout=30
    ):
        return self.wait_for_condition_with_refresh(
            lambda driver:
            self.get_today_counter() > previous_value,
            timeout=timeout
        )

    def is_order_number_in_progress(
        self,
        order_number,
        timeout=20
    ):
        order_locator = (
            OrderFeedPageLocators.order_number(
                order_number
            )
        )

        try:
            return self.wait_for_condition_with_refresh(
                lambda driver:
                self.find_element(
                    order_locator,
                    timeout=1
                ).is_displayed(),
                timeout=timeout
            )

        except TimeoutException:
            return False