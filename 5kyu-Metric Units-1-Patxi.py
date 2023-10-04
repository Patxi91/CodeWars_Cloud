def meters(x):
    prefixes = ["", "k", "M", "G", "T", "P", "E", "Z", "Y"]
    index = 0

    while x >= 1000 and index < len(prefixes) - 1:
        x /= 1000.0
        index += 1

    if int(x) == x:
        return f"{int(x)}{prefixes[index]}m"
    else:
        return f"{x:.3f}".rstrip("0").rstrip(".") + f"{prefixes[index]}m"
