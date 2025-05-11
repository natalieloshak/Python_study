def sum_even_indexed_times_last(lst):
    return sum(lst[::2]) * lst[-1] if lst else 0


examples = [[0, 1, 7, 2, 4, 8], [1, 3, 5], [6], []]

for example in examples:
    result = sum_even_indexed_times_last(example)
    print(f"{example} => {result}")

pass
