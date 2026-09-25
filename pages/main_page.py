from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    def click_personal_account(self):
        self.click_element(
            MainPageLocators.PERSONAL_ACCOUNT_BUTTON
        )

    def click_constructor(self):
        self.click_element(
            MainPageLocators.CONSTRUCTOR_BUTTON
        )

    def click_order_feed(self):
        self.click_element(
            MainPageLocators.ORDER_FEED_BUTTON
        )

    def click_login_button(self):
        self.click_element(
            MainPageLocators.LOGIN_BUTTON
        )

    def click_buns_section(self):
        self.click_element_js(
            MainPageLocators.BUNS_SECTION
        )

        self.wait_for_condition(
            lambda driver: self.is_buns_section_active()
        )

    def click_sauces_section(self):
        self.click_element_js(
            MainPageLocators.SAUCES_SECTION
        )

        self.wait_for_condition(
            lambda driver: self.is_sauces_section_active()
        )

    def click_fillings_section(self):
        self.click_element_js(
            MainPageLocators.FILLINGS_SECTION
        )

        self.wait_for_condition(
            lambda driver: self.is_fillings_section_active()
        )

    def is_buns_section_active(self):
        element = self.find_element(
            MainPageLocators.BUNS_SECTION
        )

        parent = element.find_element(
            'xpath',
            '..'
        )

        return 'tab_tab_type_current' in parent.get_attribute('class')

    def is_sauces_section_active(self):
        element = self.find_element(
            MainPageLocators.SAUCES_SECTION
        )

        parent = element.find_element(
            'xpath',
            '..'
        )

        return 'tab_tab_type_current' in parent.get_attribute('class')

    def is_fillings_section_active(self):
        element = self.find_element(
            MainPageLocators.FILLINGS_SECTION
        )

        parent = element.find_element(
            'xpath',
            '..'
        )

        return 'tab_tab_type_current' in parent.get_attribute('class')

    def click_first_ingredient(self):
        self.click_element_js(
            MainPageLocators.FIRST_INGREDIENT
        )

    def is_ingredient_modal_open(self):
        return self.find_element(
            MainPageLocators.INGREDIENT_MODAL_TITLE
        ).is_displayed()

    def close_ingredient_modal(self):
        self.click_element(
            MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON
        )

    def wait_ingredient_modal_closed(self):
        return self.wait_for_element_invisible(
            MainPageLocators.INGREDIENT_MODAL_TITLE
        )

    def drag_first_ingredient_to_constructor(self):
        ingredient = self.find_element(
            MainPageLocators.FIRST_INGREDIENT
        )

        constructor = self.find_element(
            MainPageLocators.CONSTRUCTOR_DROP_ZONE
        )

        script = """
        const source = arguments[0];
        const target = arguments[1];

        const dataTransfer = new DataTransfer();

        source.dispatchEvent(
            new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            })
        );

        target.dispatchEvent(
            new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            })
        );

        target.dispatchEvent(
            new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            })
        );

        target.dispatchEvent(
            new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            })
        );

        source.dispatchEvent(
            new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            })
        );
        """

        self.driver.execute_script(
            script,
            ingredient,
            constructor
        )

        self.wait_for_condition(
            lambda driver:
            self.get_first_ingredient_counter() == '2'
        )

    def get_first_ingredient_counter(self):
        return self.get_text(
            MainPageLocators.FIRST_INGREDIENT_COUNTER
        )

    def click_order_button(self):
        self.click_element(
            MainPageLocators.ORDER_BUTTON
        )

    def get_created_order_number(self):
        def order_number_loaded(driver):
            text = self.get_text(
                MainPageLocators.CREATED_ORDER_NUMBER
            )

            clean_number = text.replace('#', '').strip()

            if clean_number.isdigit() and clean_number != '9999':
                return clean_number

            return False

        return self.wait_for_condition(
            order_number_loaded,
            timeout=20
        )