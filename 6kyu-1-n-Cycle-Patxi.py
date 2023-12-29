def cycle(n):
    if n % 2 == 0 or n % 5 == 0:
        return -1  # n and 10 are not coprimes

    remainder_seen = {}
    remainder = 1 % n
    position = 0

    while remainder != 0 and remainder not in remainder_seen:
        remainder_seen[remainder] = position
        remainder = (remainder * 10) % n
        position += 1

    if remainder == 0:
        return 0  # No repeating cycle, decimal terminates
    else:
        return position - remainder_seen[remainder]
