number = int(input("Введіть будь-яке числове значення: "))

while number > 9:
    text = str(number)
    dobutok = 1

    for character in text:
        dobutok = dobutok * int(character)

    number = dobutok

print("Результат:", number)
