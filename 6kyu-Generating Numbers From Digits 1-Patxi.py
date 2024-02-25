from math import factorial
from functools import reduce
import operator


def proc_arr(arr):
    # Count the occurrences of each digit
    counts = {digit: arr.count(digit) for digit in arr}

    # Calculate the number of different numbers
    num_diff_numbers = factorial(len(arr)) // reduce(operator.mul, (factorial(count) for count in counts.values()), 1)

    # Calculate the minimum and maximum numbers
    min_number = int(''.join(sorted([digit for digit in arr if digit != '0'] + [digit for digit in arr if digit == '0'])))
    max_number = int(''.join(sorted(arr, reverse=True)))

    return [num_diff_numbers, min_number, max_number]
