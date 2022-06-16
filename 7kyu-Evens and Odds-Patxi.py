def evens_and_odds(n):
    if n % 2 == 0:
        return str(bin(n))[2:]
    else:
        return str(hex(n))[2:]
