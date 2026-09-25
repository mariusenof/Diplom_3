import allure

from pages.main_page import MainPage
from urls import MAIN_URL


@allure.suite('Счётчик ингредиента')
class TestIngredientCounter:

    @allure.title(
        'Счётчик ингредиента увеличивается после добавления в конструктор'
    )
    def test_ingredient_counter_increases_after_drag(self, driver):
        page = MainPage(driver, MAIN_URL)
        page.open()

        page.drag_first_ingredient_to_constructor()

        assert page.get_first_ingredient_counter() == '2'