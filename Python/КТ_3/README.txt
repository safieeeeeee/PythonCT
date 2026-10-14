КТ 3. Парсинг файла CSV

Запуск примера: python main.py

В books.csv перенесены все восемь книг из таблицы в задании.
Отдельного исходного CSV в папке с заданиями не было.
Разделитель полей — вертикальная черта |, кодировка — UTF-8.
Первая строка содержит заголовок.

Функции находятся в books.py:

get_books("books.csv")
Возвращает список списков [isbn, title, author, quantity, price].
quantity становится целым числом, price — числом с дробной частью.

filtered_books(books, "python")
Отбирает книги по подстроке в названии без учёта регистра.
Возвращает [isbn, title + ", " + author, quantity, price].
Название и автор объединены в один элемент, как требует задание.

calculate_totals(books)
Возвращает список кортежей (isbn, quantity * price).
Принимает и полный каталог, и результат filtered_books.

Пример использования:
from books import get_books, filtered_books, calculate_totals
books = get_books("books.csv")
selected = filtered_books(books, "python")
result = calculate_totals(selected)

В решении нет циклов, генераторов и списковых включений.
Преобразования выполнены с помощью map и filter.
