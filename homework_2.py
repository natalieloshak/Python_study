number = int(input("Введіть 5-значне число: "))
digit1 = number // 10000
digit2 = (number // 1000) % 10
digit3 = (number // 100) % 10
digit4 = (number // 10) % 10
digit5 = number % 10
reversed_numbers = digit5 * 10000 + digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1
print(reversed_numbers)
