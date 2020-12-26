def index_equals_value(arr):
    try:
        l, u = 0, len(arr)

        while l <= u:
            m = (l + u) // 2
            if m == arr[m] and m - 1 != arr[m - 1]:
                return m
            elif m > arr[m]:
                l = m + 1
            else:
                u = m - 1

        return -1
    except:
        pass
        return -1