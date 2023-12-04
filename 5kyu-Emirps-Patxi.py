import math

def is_prime_sup_check(k):
    return k % 2 and all(
        k % i
        for i in range(3, int(math.sqrt(k)) + 1, 2)
    )

def generate_next_prime(i):
    while True:
        if is_prime_sup_check(i - 1):
            yield i - 1

        if is_prime_sup_check(i + 1):
            yield i + 1

        i += 6

def memoized_decorator(func):
    cache_set = set()
    covered_value = 0
    prime_iterator = 18

    def custom_inner_function(n, *args):
        nonlocal covered_value, prime_iterator, cache_set

        if n > covered_value:
            updated_values, current_prime, result = func(n, cache_set, prime_iterator)
            cache_set.update(updated_values)

            prime_iterator = current_prime - (current_prime % 6)
            covered_value = n
            return result

        cached_values = [x for x in cache_set if x < n]
        return [len(cached_values), max(cached_values), sum(cached_values)]

    return custom_inner_function

@memoized_decorator
def find_emirp(n, emirps_set, i=18):
    current_value = 13
    prime_gen = generate_next_prime(i)

    while current_value < n:
        reversed_emirp = int(str(current_value)[::-1])
        if reversed_emirp != current_value and is_prime_sup_check(reversed_emirp):
            emirps_set.add(current_value)

        current_value = next(prime_gen)

    if not emirps_set:
        return emirps_set, current_value, [0, 0, 0]

    return emirps_set, current_value, [len(emirps_set), max(emirps_set), sum(emirps_set)]
