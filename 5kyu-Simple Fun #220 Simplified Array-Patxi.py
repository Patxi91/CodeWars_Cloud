def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def simplified_array(arr):
    while True:
        i = 0
        intervals = []
        while i < len(arr):
            if is_prime(arr[i]):
                j = i
                while j < len(arr) and is_prime(arr[j]):
                    j += 1
                intervals.append((i, j))
            else:
                j = i
                while j < len(arr) and not is_prime(arr[j]):
                    j += 1
                intervals.append((i, j))
            i = j

        new_arr = []
        for start, end in intervals:
            if is_prime(arr[start]):
                new_arr.append(sum(arr[start:end]))
            else:
                new_arr.append(sum(arr[start:end]))

        if new_arr == arr:
            return arr
        else:
            arr = new_arr
