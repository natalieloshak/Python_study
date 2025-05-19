import string

user_input = input("Введіть 2 букви через дефіс: ")

start_char, end_char = user_input.split("-")

all_letters = string.ascii_letters

start_index = all_letters.index(start_char)
end_index = all_letters.index(end_char)

result = all_letters[start_index : end_index + 1]
print(result)
