def stringClean(string):
    if not string:
        return ""
    if len(string) == 1:
        return string
    if string[0] == string[1]:
        return stringClean(string[1:])
    return string[0] + stringClean(string[1:])

def unique_in_order(iterable):
    return list(stringClean(iterable)) if isinstance(iterable, list) == False else list(stringClean(''.join([str(int) for int in iterable]))) if isinstance(iterable[0], str) else [int(s) for s in stringClean(''.join([str(int) for int in iterable]))]
