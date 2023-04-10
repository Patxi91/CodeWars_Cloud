def greatest_distance(arr):
    max_dist = 0
    seen = {}
    for i, num in enumerate(arr):
        if num in seen:
            dist = i - seen[num]
            if dist > max_dist:
                max_dist = dist
        else:
            seen[num] = i
    return max_dist
