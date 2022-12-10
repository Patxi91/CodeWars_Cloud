import numpy as np


def ride(group, comet):
    if np.prod([ord(l)-64 for l in group]) % 47 == np.prod([ord(l)-64 for l in comet]) % 47:
        return "GO"
    else:
        return "STAY"
