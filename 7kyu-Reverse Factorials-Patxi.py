def reverse_factorial(num):
    current_num = 1
    factorial_count = 1

    while current_num < num:
        factorial_count += 1
        current_num *= factorial_count

    if current_num == num:
        return f"{factorial_count}!"
    else:
        return "None"
