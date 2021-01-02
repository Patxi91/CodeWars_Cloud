from nose.tools import assert_equal
import math


def how_many_times_small(a, b):
    arr = [min(a, b), max(a, b)]
    count = 0
    while arr[0] > 0:
        if (arr[1] % arr[0]) == 0:
            count += 1
        arr = [x - 1 for x in arr]
    return count


def how_many_times(a, b):
    if min(a, b) == 0:
        return 0
    if a == b:
        return a
    if min(a, b) == 1:
        return 1
    elif min(a, b) < 100000:
        return how_many_times_small(a, b)

    arr = [min(a, b), max(a, b)]
    diff = arr[1] - arr[0]
    count = 0
    seed = 1

    if arr[0] > diff:
        arr[0] = diff
        arr[1] = diff * 2

    if max(a, b) % min(a, b) == 0:
        count += 1
    elif arr[1] % arr[0] == 0 and diff > 2:
        count += 1

    if diff > 2:
        lim = math.ceil(math.sqrt(diff))
    else:
        lim = math.ceil(math.sqrt(diff)) - 1

    while seed <= math.ceil(math.sqrt(diff)):
        if (diff + seed) % seed == 0:
            count += 1
            if arr[0] > diff / seed > math.ceil(math.sqrt(diff)):
                count += 1
        seed += 1
    return count


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




