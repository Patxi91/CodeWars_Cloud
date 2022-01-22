def count_duplicates(name,age,height):
    seen = []
    c = 0
    for i in range(len(name)):
        if [name[i], age[i], height[i]] in seen:
            c += 1
        else:
            seen.append([name[i], age[i], height[i]])
    return c
