def cycle(d, v, c):
    # Find the index of the current value in the list
    try:
        index = v.index(c)
    except ValueError:
        return None  # Value not found in the list

    # Calculate the next index based on the direction
    if d > 0:
        index = (index + 1) % len(v)
    elif d < 0:
        index = (index - 1) % len(v)

    # Return the value at the calculated index
    return v[index]
