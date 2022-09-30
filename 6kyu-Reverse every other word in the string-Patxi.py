def reverse_alternate(string):
    r = []
    for i, sub in enumerate(string.split()):
        if i % 2 != 0:
            r.append(sub[::-1])
        else:
            r.append(sub)

    return ' '.join(r)
