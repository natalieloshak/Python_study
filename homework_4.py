def change_last_to_first(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + lst[:-1]


# для перевірки коду
print(change_last_to_first([1]))
print(change_last_to_first([]))
print(change_last_to_first([12, 3, 4, 10, 8]))
print(change_last_to_first([12, 3, 4, 10]))
