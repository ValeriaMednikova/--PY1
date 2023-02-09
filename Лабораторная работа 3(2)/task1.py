class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, pages: int):
        super().__init__(name='Белые ночи', author='Достоевский')
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self.pages

    @pages.setter
    def pages(self, pages_: int):
        """Устанавливает количество страниц в книге."""
        if not isinstance(pages_, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages_ <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages_

    def __repr__(self):
        super().__repr__()


class AudioBook(Book):
    def __init__(self, duration: float):
        super().__init__(name='Белые ночи', author='Достоевский')
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность книги."""
        return self.duration

    @duration.setter
    def duration(self, duration_: float) -> None:
        """Устанавливает продолжительность книги."""
        if not isinstance(duration_, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration_ <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self.duration = duration_

    def __repr__(self):
        super().__repr__()
# для сохранения последней строки
