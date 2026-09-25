import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    def click_constructor(self):
        overlay_locator = (
            'xpath',
            "//div[contains(@class, 'Modal_modal_overlay')]"
        )

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.invisibility_of_element_located(
                overlay_locator
            )
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
        end_time = time.time() + timeout

        while time.time() < end_time:
            current_value = self.get_total_counter()

            if current_value > previous_value:
                return True

            self.driver.refresh()
            time.sleep(1)

        return False

    def wait_today_counter_increased(
        self,
        previous_value,
        timeout=30
    ):
        end_time = time.time() + timeout

        while time.time() < end_time:
            current_value = self.get_today_counter()

            if current_value > previous_value:
                return True

            self.driver.refresh()
            time.sleep(1)

        return False

    def is_order_number_in_progress(
        self,
        order_number
    ):
        self.find_element(
            OrderFeedPageLocators.ORDERS_IN_PROGRESS_TITLE
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