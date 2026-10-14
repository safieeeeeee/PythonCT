import csv


def parse_book(row):
    return [row[0], row[1], row[2], int(row[3]), float(row[4])]


def get_books(filename):
    with open(filename, encoding="utf-8-sig", newline="") as file:
        rows = csv.reader(file, delimiter="|")
        next(rows, None)
        return list(map(parse_book, filter(any, rows)))


def filtered_books(books, text):
    matching = filter(lambda book: text.casefold() in book[1].casefold(), books)
    return list(map(
        lambda book: [book[0], book[1] + ", " + book[2], book[3], book[4]],
        matching
    ))


def calculate_totals(books):
    return list(map(lambda book: (book[0], book[-2] * book[-1]), books))
