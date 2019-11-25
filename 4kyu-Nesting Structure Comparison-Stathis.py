def same_structure_as(original,other):
    if isinstance(original,list) != isinstance(other,list):
        return False
    elif isinstance(original,int) == True and isinstance(other,int) == True:
        return True
    elif isinstance(original,list) and isinstance(other,list) and len(original) != len(other):
        return False
    elif isinstance(original,list) and isinstance(other,list):
        return all([same_structure_as(s1,s2) for s1,s2 in zip(original,other)])
    else:
        return True
