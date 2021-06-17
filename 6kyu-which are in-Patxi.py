def in_array(a1, a2):
    return sorted(list(set([ela1 for ela1 in a1 if max([ela1 in ela2 for ela2 in a2])]))) if a1 and a2 else []
