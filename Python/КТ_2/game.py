from pathlib import Path
from random import choice


folder = Path(__file__).resolve().parent
word = ""
letters = []
errors = 0
max_errors = 7
active = False
interrupted = False


def load_words():
    words = []
    with open(folder / "words.txt", encoding="utf-8-sig") as file:
        for line in file:
            candidate = line.strip().lower()
            if candidate.isalpha():
                words.append(candidate)
    return words


def show_word():
    visible = []
    for letter in word:
        if letter in letters:
            visible.append(letter.upper())
        else:
            visible.append("_")
    print("Слово: " + " ".join(visible))


def word_is_guessed():
    for letter in word:
        if letter not in letters:
            return False
    return True


def show_gallows():
    path = folder / "stages" / f"stage_{errors}.txt"
    with open(path, encoding="utf-8") as file:
        print(file.read())


def start_game():
    global word, letters, errors, active, interrupted
    word = ""
    letters = []
    errors = 0
    active = False
    interrupted = False

    try:
        words = load_words()
    except OSError:
        print("Не удалось открыть words.txt. Положи файл рядом с main.py.")
        return

    if not words:
        print("Добавь в words.txt хотя бы одно слово из букв.")
        return

    word = choice(words)
    active = True
    print("Игра «Виселица на поле чудес»")
    print("Дамир, отгадай слово по буквам. Можно сделать семь ошибок.")
    show_word()


def is_playing():
    return active


def play_turn():
    global errors, active, interrupted

    try:
        letter = input("Назови букву: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        interrupted = True
        active = False
        print("\nИгра прервана.")
        return

    if len(letter) != 1 or not letter.isalpha():
        print("Введи одну букву.")
        return

    if letter in letters:
        print("Эту букву уже называли.")
        return

    letters.append(letter)

    if letter in word:
        print("Есть такая буква!")
    else:
        errors += 1
        print("Такой буквы нет.")
        show_gallows()

    show_word()
    print("Названные буквы: " + ", ".join(letters))
    print(f"Ошибок: {errors} из {max_errors}.")

    if errors == max_errors or word_is_guessed():
        active = False


def finish_game():
    if interrupted or not word:
        return

    if word_is_guessed():
        print(f"Победа, Дамир! Загаданное слово: {word.upper()}.")
    else:
        print(f"Игра окончена. Загаданное слово: {word.upper()}.")
