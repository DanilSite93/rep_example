import json
from datetime import datetime

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        converted_date_obj = None
        # Если год представлен целым числом:
        if isinstance(self.year, int):
            converted_date_obj = datetime(year=self.year, month=1, day=1)
        # Если год представлен строкой:
        elif isinstance(self.year, str):
            return "Не работает с строками"

        # Преобразование года в две цифры с учётом того, что года ранее 1900 не поддерживаются функцией strftime:
        converted_date_obj = converted_date_obj.replace(
            year=converted_date_obj.year + 1900)
        last_two_digits = converted_date_obj.strftime('%y')

        # Создание словаря с информацией о книге:
        book_info = {
            "name": self.name,
            "author": self.author,
            "year": last_two_digits
        }

        # Возврат информации о книге в формате JSON в виде строки
        return json.dumps(book_info)
    def get_age(self):
        """Возвращает возраст книги в годах"""
        current_year = datetime.now().year
        year_int = self.year if isinstance(self.year, int) else int(self.year)
        return current_year - year_int

#
book_2 = Book("The Road", "Cormac McCarthy", "2006")
book_3 = Book("Kapitanskaya Dochka", "Pushkin", 1836)
book_4 = Book("Евгений Онегин", "А.С. Пушкин", "1925")

# Вывод информации о книгах
print(book_1)
print(book_2)
print(book_3)
print(book_4)
print("Возраст book_1:", book_1.get_age())
print("Возраст book_3:", book_3.get_age())
