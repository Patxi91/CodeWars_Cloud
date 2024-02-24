from collections import defaultdict

# Precompute perfect squares
sorted_squares_dict = defaultdict(list)
for number in range(4, 10000):
    sorted_square_str = ''.join(sorted(str(number * number)))
    if '0' not in sorted_square_str:
        sorted_squares_dict[sorted_square_str].append(number * number)

sorted_squares_list = []
for squares in sorted_squares_dict.values():
    [sorted_squares_list.append((square, len(squares), squares[-1])) for square in squares]
sorted_squares_list.sort()


def next_perfectsq_perm(lower_limit, count):
    for current_square, group_size, max_square_in_group in sorted_squares_list:
        if lower_limit < current_square and group_size == count:
            return max_square_in_group
