def get_unique_list_numbers() -> list[int]:
    import random
    random_list = random.sample(range(-10, 11), 15)

    return random_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# для сохранения последней строки
