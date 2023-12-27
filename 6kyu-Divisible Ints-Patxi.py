def get_count(n):
    if n == 0:
        return 0

    n_str = str(n)
    count = 0

    for i in range(len(n_str)):
        for j in range(i + 1, len(n_str) + 1):
            substring = int(n_str[i:j])
            if substring != n and substring != 0 and n % substring == 0:
                count += 1

    return count
