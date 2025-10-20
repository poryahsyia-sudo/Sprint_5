import random
import string


def generate_email(first_name="Anastassiya", last_name="Makiyeko", cohort="32"):
    random_digits = random.randint(100, 999)
    return f"{first_name}_{last_name}_{cohort}_{random_digits}@yandex.ru"


def generate_password(length=8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))
