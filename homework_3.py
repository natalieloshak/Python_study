digit1 = int(input("Вкажіть перше число: "))
operation = input("Оберіть математичну дію (+, -, *, /): ")
digit2 = int(input("Вкажіть друге число: "))

if operation == "+":
    print("Результат:", int(digit1 + digit2))
elif operation == "-":
    print("Результат:", int(digit1 - digit2))
elif operation == "*":
    print("Результат:", int(digit1 * digit2))
elif operation == "/":
    if digit2 == 0:
        print("Помилка: ділити на нуль не можна! Спробуйте ще раз. ")
    else:
        print("Результат:", int(digit1 / digit2))
else:
    print("Обрана невірна математична дія. Введіть +, -, * або /.")
