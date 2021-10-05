def div_sum(n):
    divs = set()
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            divs.add(x)
            divs.add(n // x)
    return sum(divs)


def buddy(start, limit):
    for n in range(start, limit+1):
        buddy = div_sum(n)

        if buddy > n and div_sum(buddy) == n:
            return [n, buddy]

    return "Nothing"
