def is_valid_coordinates(coordinates):
    try:
        la = "".join(coordinates.split(", ")[0].strip())
        lo = "".join(coordinates.split(", ")[1].strip())
        if any(c.isalpha() for c in la):
            return False
        if any(c.isalpha() for c in lo):
            return False
        la = float(la)
        lo = float(lo)
        return True if (-90 <= la <= 90 and -180 <= lo <= 180) else False
    except:
        return False
    return True if (-90 <= la <= 90 and -180 <= lo <= 180) else False
