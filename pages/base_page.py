from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable_element(self, locator, timeout=10):
        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.element_to_be_clickable(locator)
        )

    def click_element(self, locator, timeout=10):
        self.find_clickable_element(
            locator,
            timeout
        ).click()

    def click_element_js(self, locator, timeout=10):
        element = self.find_element(
            locator,
            timeout
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def get_text(self, locator, timeout=10):
        return self.find_element(
            locator,
            timeout
        ).text

    def wait_for_url(self, url, timeout=10):
        expected_url = url.rstrip('/')

        WebDriverWait(
            self.driver,
            timeout
        ).until(
            lambda driver:
            driver.current_url.rstrip('/') == expected_url
        )

    def wait_for_condition(self, condition, timeout=10):
        return WebDriverWait(
            self.driver,
            timeout
        ).until(condition)

    def wait_for_element_invisible(self, locator, timeout=10):
        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.invisibility_of_element_located(locator)
        )

    def current_url(self):
        return self.driver.current_url