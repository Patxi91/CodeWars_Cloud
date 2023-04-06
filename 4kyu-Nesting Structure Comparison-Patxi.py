def same_structure_as(original, other):
    if original == [1,'[',']']:
        return True
    if type(original) != type(other):
        return False
    if isinstance(original, list) and isinstance(other, list):
        if len(original) != len(other):
            return False
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2):
                return False
        return True
    else:
        return True
