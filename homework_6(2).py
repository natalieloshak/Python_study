seconds = int(input("Введіть кількість секунд від 0 до 8640000 включно: "))

days = seconds // 86400
seconds = seconds % 86400

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in [2, 3, 4] and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"


print(
    str(days)
    + " "
    + day_word
    + ", "
    + str(hours).zfill(2)
    + ":"
    + str(minutes).zfill(2)
    + ":"
    + str(seconds).zfill(2)
)
