from pages.base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):

    def enter_email(self, email):
        element = self.find_element(
            LoginPageLocators.EMAIL_INPUT
        )
        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        element = self.find_element(
            LoginPageLocators.PASSWORD_INPUT
        )
        element.clear()
        element.send_keys(password)

    def click_login_button(self):
        self.wait_for_element_invisible(
            LoginPageLocators.MODAL_OVERLAY
        )

        self.click_element_js(
            LoginPageLocators.LOGIN_BUTTON
        )

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()