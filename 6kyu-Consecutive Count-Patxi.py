
def get_consective_items(items, key):
    s = 0
    m = 0

    for i in str(items):
        if i == str(key):
            s += 1
        else:
            if s > m:
                m = s
            s = 0

    return max(s, m)
