import allure

from pages.main_page import MainPage
from urls import MAIN_URL


@allure.suite('Модальное окно ингредиента')
class TestIngredientModal:

    @allure.title(
        'Открытие модального окна ингредиента'
    )
    def test_click_ingredient_opens_modal(self, driver):
        page = MainPage(
            driver,
            MAIN_URL
        )

        page.open()

        page.click_first_ingredient()

        assert page.is_ingredient_modal_open()

    @allure.title(
        'Закрытие модального окна ингредиента'
    )
    def test_close_ingredient_modal(self, driver):
        page = MainPage(
            driver,
            MAIN_URL
        )

        page.open()

        page.click_first_ingredient()
        page.close_ingredient_modal()

        assert page.wait_ingredient_modal_closed()