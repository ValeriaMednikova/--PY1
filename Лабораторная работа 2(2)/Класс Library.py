from pydantic import BaseModel
from typing import Optional
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not isinstance(id_, int):
            raise TypeError()
        if id_ < 0:
            raise ValueError()
        self.id = id_

        if not isinstance(name, str):
            raise TypeError()
        self.name = name

        if not isinstance(pages, int):
            raise TypeError()
        if pages <= 0:
            raise ValueError()
        self.pages = pages


# написать класс Library
class Library (BaseModel):
    books: Optional[list]

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        """
        if self.books is None:
            return 1
        else:
            return BOOKS_DATABASE[1]["id"]+1

    def get_index_by_book_id(self, id_2: int) -> int:
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
        """
        if self.books is not None:
            for i, j in enumerate(BOOKS_DATABASE):
                if j['id'] == id_2:
                    return i
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
# для сохранения последней строки
