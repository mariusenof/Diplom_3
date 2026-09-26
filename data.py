import random
import string


def generate_random_string(length=10):
    return ''.join(
        random.choice(string.ascii_lowercase)
        for _ in range(length)
    )


def generate_user_data():
    random_part = generate_random_string()

    return {
        'email': f'{random_part}@yandex.ru',
        'password': generate_random_string(),
        'name': generate_random_string()
    }