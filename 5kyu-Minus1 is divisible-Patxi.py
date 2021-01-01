from nose.tools import assert_equal
from copy import copy
import math


def how_many_times1(a, b):
    if a == 0  or b == 0:
        return 0
    if a == b:
        return a
    my_set = set([min(a, b), max(a, b)])
    old_set = set()
    count = 0
    while min(my_set) > 0:
        if (max(my_set) % min(my_set)) == 0:
            count += 1
        old_set = copy(my_set)
        my_set.clear()
        my_set.update([min(old_set)-1, max(old_set)-1])
    return count


def how_many_times2(a, b):
    if a == 0  or b == 0:
        return 0
    if a == b:
        return a

    arr = [min(a, b), max(a, b)]
    count = 0
    while arr[0] > 0:
        if (arr[1] % arr[0]) == 0:
            count += 1
            print(arr)
        arr = [x - 1 for x in arr]
    return count


def how_many_times(a, b):
    if a == 0  or b == 0:
        return 0
    if a == b:
        return a

    arr = [min(a, b), max(a, b)]
    diff = arr[1] - arr[0]
    count = 0
    print(f'Case a={a} and b={b}:')
    while arr[0] > 0:
        '''
        if arr[0] > 100 and arr[0] > arr[1] / 2:
            arr[1] = math.ceil(arr[1] / 2)
            arr[0] = arr[1] - diff
        '''
        if arr[0] > 100000 and arr[0] > arr[1] / 2:
            arr[1] = math.ceil(arr[1] / 2)
            arr[0] = arr[1] - diff

        if (arr[1] % arr[0]) == 0:
            count += 1
            if arr[0] > 100000:
                arr[0] = math.ceil(arr[1] / 6)
                arr[1] = arr[0] + diff
            print(arr)
        arr = [x - 1 for x in arr]
    return count


def is_divisible(a, b):
    return a % b == 0


def how_many_times3(a, b):
    if a == b:
        return a

    smaller = min(a, b)
    larger = max(a, b)

    floordiv = (larger // smaller) + 1
    if not is_divisible(larger, smaller):
        removable = (smaller * floordiv) - larger
        smaller -= removable
        larger -= removable

    counter = 0

    while smaller > 0:
        if is_divisible(larger, smaller):
            counter += 1
        smaller -= 1
        larger -= 1

    return counter


class Test:

    def test(self, function):
        assert_equal(function(3, 5), 2)
        assert_equal(function(10, 1), 1)
        assert_equal(function(7, 7), 7)
        assert_equal(function(16, 32), 5)
        assert_equal(function(42, 21), 4)
        assert_equal(function(54, 17), 1)
        assert_equal(function(150080, 150032), 10)
        assert_equal(function(654093782, 937618402), 24)
        assert_equal(function(1000000000, 649735194), 16)
        print('ALL TEST CASES PASSED')


t = Test()
t.test(how_many_times)




