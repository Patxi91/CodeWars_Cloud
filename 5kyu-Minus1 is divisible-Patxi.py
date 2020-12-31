from nose.tools import assert_equal


def how_many_times1(a, b):
    if a == 0  or b == 0:
        return 0
    if a == b:
        return a

    arr = [min(a,b), max(a,b)]
    count = 0
    while arr[0] > 0:
        if (arr[1] % arr[0]) == 0:
            count += 1
        arr = [x - 1 for x in arr]
    return count


def how_many_times(a, b):
    pass


class Test:

    def test(self, function):
        assert_equal(function(3, 5), 2)
        assert_equal(function(10, 1), 1)
        assert_equal(function(7, 7), 7)
        assert_equal(function(16, 32), 5)
        assert_equal(function(42, 21), 4)
        assert_equal(function(54, 17), 1)
        assert_equal(function(150080, 150032), 10)
        print('ALL TEST CASES PASSED')


t = Test()
t.test(how_many_times)




