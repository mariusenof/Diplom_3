import allure

from pages.main_page import MainPage
from urls import MAIN_URL


@allure.suite('Конструктор')
class TestConstructor:

    @allure.title('Переход в раздел Соусы')
    def test_click_sauces_opens_sauces_section(self, driver):
        page = MainPage(driver, MAIN_URL)
        page.open()

        page.click_sauces_section()

        assert page.is_sauces_section_active()

    @allure.title('Переход в раздел Начинки')
    def test_click_fillings_opens_fillings_section(self, driver):
        page = MainPage(driver, MAIN_URL)
        page.open()

        page.click_fillings_section()

        assert page.is_fillings_section_active()

    @allure.title('Переход обратно в раздел Булки')
    def test_click_buns_opens_buns_section(self, driver):
        page = MainPage(driver, MAIN_URL)
        page.open()

        page.click_sauces_section()
        page.click_buns_section()

        assert page.is_buns_section_active()