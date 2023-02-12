if __name__ == "__main__":
    class Cosmetic:
        """ Базовый класс косметика. """
        def __init__(self, brand: str, manufacturer: str, price: (int, float)) -> None:
            """
            Создание и подготовка к работе объекта "Косметика"
            :param brand: Название бренда (марка)
            :param manufacturer: Производитель
            :param price: Цена
            """
            if not isinstance(brand, str):
                raise TypeError("Название бренда указано неверно")
            if not isinstance(manufacturer, str):
                raise TypeError("Производитель указан неверно")
            if not isinstance(price, (int, float)):
                raise TypeError("Цена неверно указана")
            if price < 0:
                raise ValueError("Цена не может быть отрицательным числом")
            self.brand = brand
            self.manufacturer = manufacturer
            self.price = price

        def cost(self) -> str:
            """
            Функция, определяющая сегмент объекта "Косметика"
            """
            if self.price > 2000:
                return 'Люкс-сегмент'
            elif (self.price > 1000) and (self.price < 2000):
                return 'Средний ценовой сегмент'
            else:
                return 'Бюджетный сегмент'

        def __str__(self):
            return f"Название бренда {self.brand}. Производитель {self.manufacturer}"

        def __repr__(self):
            return f"{self.__class__.__name__}(brand={self.brand!r}, author={self.manufacturer!r})"


    class Mascara(Cosmetic):
        """ Базовый класс тушь для ресниц. """
        def __init__(self, type_: str) -> None:
            """
            Создание и подготовка к работе объекта "Косметика"
            :param type_: Тип туши
            """
            super().__init__(brand='PUPA', manufacturer='Италия', price=1200)
            self.type_ = type_

        @property
        def type_(self) -> str:
            """Возвращает тип туши (назначение продукта)."""  # Например, для удлинения ресниц
            return self.type_

        @type_.setter
        def type_(self, type_1: str) -> None:
            """Устанавливает назначение продукта."""
            if not isinstance(type_1, str):
                raise TypeError("Неверный формат")
            self.type_1 = type_1

        def __repr__(self):
            super().__repr__()

        def cost(self):
            super().cost()
    pass
# для сохранения последней строки
