import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file, delimiter=',', new_line='\n') -> list[dict]:
    with open(file, "r") as f:
        lst = []  # формируем список для словарей
        for i, string in enumerate(f):  # каждому номеру строки будет соответсвовать строка
            column = string.strip(new_line).split(delimiter)  # формируем столбец
            if i == 0:
                heading = column  # если это заголовок, то записываем его в отдельную переменную
            lst.append({})  # добавляем новый словарь
            for j, _ in enumerate(heading):
                lst[-1][heading[j]] = column[j]  # сопоставляем последнему элементу в списке заголовок
        return lst


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
#  для сохранения последней строки
#  не знаю, как убрать из кода первый словарь с парами заголовок-заголовок
