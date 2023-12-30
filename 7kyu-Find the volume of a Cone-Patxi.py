import math

def volume(r, h):
    # Calculate the volume using the formula
    v = (1/3) * math.pi * r**2 * h

    # Round down the volume to an integer
    v = int(v)

    return v
