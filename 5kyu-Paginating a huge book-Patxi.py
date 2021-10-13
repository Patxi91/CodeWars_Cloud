import math


def page_digits(pages):
    # Cache 1-9
    cache, k = {}, 1
    for v in range(1, 10):
        cache[k] = v
        k += 1

    if pages not in cache and pages < 1000000:
        for page in range(10, pages + 1):
            cache[page] = len(str(page)) + cache[page - 1]
        return cache[pages]

    elif pages not in cache:
        # Populating large cache
        start = 1000000
        cache[start] = 5888894
        while len(str(pages)) != len(str(start)):
            next = 10 * start
            cache[next] = cache[start] + (len(str(start)) * start * 9) + 1
            start = next
        return cache[start] + (len(str(start)) * (pages - start)) + 2

    return cache[pages]
