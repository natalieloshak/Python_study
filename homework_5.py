def split_list(lst):
    if len(lst) == 0:
        return [[], []]
    mid = len(lst) // 2
    if len(lst) % 2 == 0:
        return [lst[:mid], lst[mid:]]
    else:
        return [lst[: mid + 1], lst[mid + 1 :]]


# перевірка коду
print(split_list([1]))
print(split_list([]))
print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
