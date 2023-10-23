def even_numbers(arr, n):
    even_nums = []
    for num in reversed(arr):
        if num % 2 == 0:
            even_nums.append(num)
            if len(even_nums) == n:
                break
    return even_nums[::-1]
