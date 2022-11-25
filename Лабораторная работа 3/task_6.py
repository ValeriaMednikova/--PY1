list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
max_value = list_numbers[max_index]  # пусть первое число будет самым максимальным

for i, value in enumerate(list_numbers):  # рассматриваем пары индекс и значение
    max_value = list_numbers[max_index]
    if value >= max_value:  # сравним значение с максимальным
        max_index = i  # перезапишем индекс максимального числа
        max_value = list_numbers[max_index]  # перезаписываем большее число

list_numbers[-1], list_numbers[max_index] = list_numbers[max_index], list_numbers[-1]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
