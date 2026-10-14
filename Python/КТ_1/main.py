from random import randint


print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")
goodbyes = 0

while True:
    try:
        phrase = input("> ")
    except EOFError:
        break

    if phrase == "ПОКА!":
        goodbyes += 1
    else:
        goodbyes = 0

    if goodbyes == 3:
        print("ДО СВИДАНИЯ, МИЛЫЙ!")
        break

    if phrase.isupper():
        year = randint(1930, 1950)
        print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
    else:
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
