import doctest
import math


class TruncatedCone:
    def __init__(self, r1: float, r2: float, height: float):
        """
        Создание и подготовка к работе объекта "Усеченный конус"
        :param r1: Нижний радиус основания
        :param r2: Верхний радиус основания
        :param height: Высота конуса
        Примеры:
        >>> cone = TruncatedCone(50, 40, 10)  # инициализация экземпляра класса
        """
        if not isinstance(r1, (int, float)):
            raise TypeError("Радиус основания должен быть int или float")
        if r1 <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        if r1 < r2:
            raise ValueError("Нижний радиус основания больше верхнего")
        self.r1 = r1

        if not isinstance(r2, (int, float)):
            raise TypeError("Радиус основания должен быть int или float")
        if r2 <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        if r2 > r1:
            raise ValueError("Нижний радиус основания больше верхнего")
        self.r2 = r2

        if not isinstance(height, (int, float)):
            raise TypeError("Высота конуса должна быть int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

    def capacity_volume(self) -> int or float:  # Объем
        """
        Функция, вычисляющая объем усеченного конуса
        :return: Объем
        Примеры:
        >>> cone = TruncatedCone(50, 40, 10)
        >>> cone.capacity_volume()
        63879.05
        """
        result = math.pi * self.height * (self.r1 ** 2 + self.r1 * self.r2 + self.r2 ** 2)/3
        return round(result, 2)

    def total_area(self) -> int or float:  # Площадь полной поверхности
        """
        Функция, вычисляющая площадь полной поверхности усеченного конуса
        :return: Площадь полной поверхности усеченного конуса
        Примеры:
        >>> cone = TruncatedCone(50, 40, 10)
        >>> cone.total_area()
        16879.12
        """
        forming_ = (self.height ** 2 + (self.r1 - self.r2) ** 2) ** (1/2)
        result_2 = math.pi * (forming_ * self.r1 + forming_ * self.r2 + self.r1 ** 2 + self.r2 ** 2)
        return round(result_2, 2)

    def side_area(self) -> int or float:  # Площадь боковой поверхности
        """
        Функция, вычисляющая площадь боковой поверхности усеченного конуса
        :return: Площадь боковой поверхности усеченного конуса
        Примеры:
        >>> cone = TruncatedCone(50, 40, 10)
        >>> cone.side_area()
        3998.59
        """
        forming_ = (self.height ** 2 + (self.r1 - self.r2) ** 2) ** (1 / 2)
        result_3 = math.pi * forming_ * (self.r1 + self.r2)
        return round(result_3, 2)

    def forming(self) -> float:  # Образующая усеченного конуса
        """
        Функция, вычисляющая образующую усеченного конуса
        :return: Образующая усеченного конуса
        Примеры:
        >>> cone = TruncatedCone(50, 40, 10)
        >>> cone.forming()
        14.14
        """
        return round(((self.height ** 2 + (self.r1 - self.r2) ** 2) ** (1 / 2)), 2)


class Glasses:
    def __init__(self, material: str, frame_color: str, diopters: float):
        """
        Создание объекта "Очки"
        :param material: Материал
        :param frame_color: Цвет оправы
        :param diopters: Величина диоптрий
        Примеры:
        >>> glasses = Glasses('Стекло прозрачное', 'Черный цвет', -2.5)
        """
        if not isinstance(material, str):
            raise TypeError("Материал не выбран")
        if ('Стекло' or 'Пластик') not in material:
            raise ValueError("Неверно задан материал")
        self.material = material

        if not isinstance(frame_color, str):
            raise TypeError("Цвет оправы не выбран")
        if 'цвет' not in frame_color:
            raise ValueError("Неверный параметр")
        self.frame_color = frame_color

        if not isinstance(diopters, (int, float)):
            raise TypeError("Неверно выбраны линзы")
        self.diopters = diopters

    def choose_glasses(self) -> bool:
        """
        Функция, определяющая нужны ли вам очки
        :return: Нужны ли очки
        Примеры:
        >>> glasses = Glasses('Стекло прозрачное', 'Черный цвет', -2.5)
        >>> glasses.choose_glasses()
        True
        """
        if self.diopters != 1:
            return True

    def type_of_violation(self) -> str:
        """
        Функция, определяющая дальнозоркость у вас или близорукость
        :return: Диагноз
        Примеры:
        >>> glasses = Glasses('Стекло прозрачное', 'Черный цвет', -2.5)
        >>> glasses.type_of_violation()
        'Близорукость'
        """
        if self.diopters < 0:
            return 'Близорукость'
        elif self.diopters > 0:
            return 'Дальнозоркость'


class Beer:
    def __init__(self, material_: str, percentage_of_alcohol: (int, float), capacity_volume: (int, float)):
        """
        Создание объекта "Пиво"
        :param material_: Материал
        :param percentage_of_alcohol: Содержание алкголя
        :param capacity_volume: Объем в литрах
        Примеры:
        >>> beer = Beer('Яблоко', 4.5, 0.5)
        """
        if not isinstance(material_, str):
            raise TypeError("Материал не выбран")
        self.material_ = material_

        if not isinstance(percentage_of_alcohol, (int, float)):
            raise TypeError("Ошибка в процентном содержании")
        if percentage_of_alcohol < 0:
            raise ValueError("Неверный параметр")
        self.percentage_of_alcohol = percentage_of_alcohol

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Ошибка в мере объема")
        if capacity_volume < 0:
            raise ValueError("Объем не может быть отрицательным")
        if capacity_volume == 0:
            raise ValueError("Пива нет")
        self.capacity_volume = capacity_volume

    def choose_drink(self) -> str:
        """
        Функция, определяющая что за напиток перед вами
        :return: Напиток
        Примеры:
        >>> beer = Beer('Яблоко', 4.5, 0.5)
        >>> beer.choose_drink()
        'Сидр'
        """
        if self.material_ == ('Яблоко' or 'Груша'):
            return 'Сидр'
        elif self.material_ == 'Хмель':
            return 'Пиво'
        else:
            return 'Это другой напиток'

    def percentage(self) -> str:
        """
        Функция, определяющая по крепости напитка что это
        :return: Напиток
        Примеры:
        >>> beer = Beer('Яблоко', 4.5, 0.5)
        >>> beer.percentage()
        'Пиво'
        """
        if self.percentage_of_alcohol == 0:
            return 'Безалкогольный напиток'
        elif self.percentage_of_alcohol > 9:
            return 'Другой алкогольный напиток'
        else:
            return 'Пиво'


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
# для сохранения последней строки
