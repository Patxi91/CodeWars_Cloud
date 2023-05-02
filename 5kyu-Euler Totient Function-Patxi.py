def totient(n):
    # Check if n is a valid input
    if not isinstance(n, int) or n < 1:
        return 0

    # Calculate the Euler totient using Euler's product formula
    result = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n

    return result
