import math


def page_digits(pages):
    # Cache 1-9
    cache, k = {}, 1
    for v in range(1, 10):
        cache[k] = v
        k += 1

    if pages not in cache and pages < 1000000:
        for page in range(10, pages + 1):
            cache[page] = int(math.log(page, 10) + 1) + cache[page - 1]

    elif pages not in cache:
        # Populating large cache
        start = 1000000
        cache[start] = 5888894
        #while int(math.log(pages, 10) + 1) != int(math.log(start + 1, 10) + 1):
        while len(str(pages)) != len(str(start)):
            next_n = 10 * start
            cache[next_n] = cache[start] + (len(str(start)) * start * 9) + 1
            start = next_n
        return cache[start] + (len(str(start)) * (pages - start))

    return cache[pages]

a = page_digits(6178533592471141)  # 1235237768727350605
