def compute_depth(n):
    if n <= 0:
        raise ValueError("n must be a positive number greater than zero.")

    digits = set()
    multiple = 0
    while len(digits) < 10:
        multiple += 1
        value = multiple * n
        for digit in str(value):
            digits.add(int(digit))

    return multiple
