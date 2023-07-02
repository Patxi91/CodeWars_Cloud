def around_fib(n):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    fib = str(fibonacci(n))
    digit_counts = [fib.count(str(digit)) for digit in range(10)]
    max_count = max(digit_counts)
    max_digit = digit_counts.index(max_count)

    chunks = [fib[i:i+25] for i in range(0, len(fib), 25)]
    last_chunk = chunks[-1]

    result = f"Last chunk {last_chunk}; Max is {max_count} for digit {max_digit}"
    return result
