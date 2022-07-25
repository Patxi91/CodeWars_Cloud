def like_or_dislike(lst):
    if not lst:
        return Nothing
    r = None
    for e in lst:
        if r == e:
            r = Nothing
        elif r != e:
            r = e
    return r
