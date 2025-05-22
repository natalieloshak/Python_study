while True:
    try:
        expression = input("Введіть математичний вираз (наприклад, 2 + 3): ")

        # Обчислення виразу
        result = eval(expression)

        print("Результат:", result)
    except Exception as e:
        print("Виникла помилка:", e)

    answer = input("Бажаєте продовжити? (y/yes для так): ").strip().lower()
    if answer not in ("y", "yes"):
        print("Роботу калькулятора завершено.")
        break
