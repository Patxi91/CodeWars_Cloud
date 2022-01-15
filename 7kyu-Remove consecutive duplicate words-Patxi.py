import itertools

def remove_consecutive_duplicates(s):
    return " ".join([k for k, g in itertools.groupby(s.split())])