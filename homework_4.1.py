def put_zeros_in_the_end(lst):
    non_zeros = [a for a in lst if a != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros


examples = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0],
]

for example in examples:
    print(f"{example} -> {put_zeros_in_the_end(example)}")
