def common(a, b, c):
    # Count the occurrences of elements in each array
    count_a = {}
    count_b = {}
    count_c = {}

    for num in a:
        count_a[num] = count_a.get(num, 0) + 1

    for num in b:
        count_b[num] = count_b.get(num, 0) + 1

    for num in c:
        count_c[num] = count_c.get(num, 0) + 1

    common_elements = set(a) & set(b) & set(c)

    total_sum = 0

    for num in common_elements:
        total_sum += num * min(count_a[num], count_b[num], count_c[num])

    return total_sum
