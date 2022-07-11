def divisions(n, divisor):
    if n == divisor:
        return 1
    count = 0
    while n > divisor:
        if n // divisor > 0:
            count = count + 1
            n = n // divisor
    return count if n!=divisor else count+1
