def sum_of_elements(arr: list, n: int) -> bool:
    sumfirst = 0
    sumsecond = 0

    for i in range(n):
        # Add elements in first half sum
        if (i < n // 2):
            sumfirst += arr[i]
        # Add elements in the second half sum
        else:
            sumsecond += arr[i]

    return sumfirst == sumsecond


def luck_check(s: str) -> bool:
    sl = [int(x) for x in [*s]]
    if len(sl) % 2 != 0:
        sl.pop(len(sl) // 2)
    return sum_of_elements(sl, len(sl))
