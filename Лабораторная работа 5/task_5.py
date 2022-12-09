def get_random_password() -> str:
    import random
    import string

    alphabet = (string.digits + string.ascii_lowercase + string.ascii_uppercase)
    random_password = random.sample(alphabet, 8)

    return "".join(map(str, random_password))


print(get_random_password())
# для сохранения последней строки
