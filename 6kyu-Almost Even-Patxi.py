def split_integer(num, parts):
    output = [num // parts for i in range(parts)]
    remainder = num % parts
    if remainder > 0:
        for i in range(remainder):
            output[i] += 1
    return sorted(output)
