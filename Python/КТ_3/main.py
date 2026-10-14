from pathlib import Path
from pprint import pprint

from books import calculate_totals, filtered_books, get_books


if __name__ == "__main__":
    catalog = get_books(Path(__file__).resolve().with_name("books.csv"))
    selected = filtered_books(catalog, "python")

    print("Каталог книг:")
    pprint(catalog, sort_dicts=False)

    print("\nКниги со словом python в названии:")
    pprint(selected, sort_dicts=False)

    print("\nISBN и стоимость всех экземпляров каждой выбранной книги:")
    pprint(calculate_totals(selected))
