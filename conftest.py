import pytest
import requests

from selenium import webdriver

from data import generate_user_data
from urls import REGISTER_API_URL, USER_API_URL


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser_name = request.param

    if browser_name == 'chrome':
        driver = webdriver.Chrome()

    elif browser_name == 'firefox':
        driver = webdriver.Firefox()

    else:
        raise ValueError(
            f'Unsupported browser: {browser_name}'
        )

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def user():
    user_data = generate_user_data()

    response = requests.post(
        REGISTER_API_URL,
        json=user_data
    )

    response_body = response.json()
    access_token = response_body.get('accessToken')

    yield user_data

    if access_token:
        requests.delete(
            USER_API_URL,
            headers={
                'Authorization': access_token
            }
        )