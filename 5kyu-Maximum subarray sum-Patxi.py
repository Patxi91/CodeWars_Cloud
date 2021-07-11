def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


def max_sequence(arr):
    if not arr:
        return 0
    elif not max([i >= 0 for i in arr]):
        return 0
    return maxSubArraySum(arr, len(arr))
