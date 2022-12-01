def calculate_optimal_fare(d, t, v1, r, v2):
    H = t/60
    if d <= H*v2:
        return '0.00'
    else:
        if v1 != v2:
            result = (H - d*1./v2)/(1./v1 - 1./v2)
        else:
            if H*v2 < d:
                return "Won't make it!"
            else:
                return '0.00'
        if result > d or result < 0:
            print(result)
            return "Won't make it!"
    return '{0:.2f}'.format(r*result)
