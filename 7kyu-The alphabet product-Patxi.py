def alphabet(lst):
    products = set()
    for a in lst:
        for b in lst:
            if a < b:
                products.add(a*b)
    remaining = set(lst) - products
    return max(remaining) if max(remaining) != 1 else alphabet([n for n in lst if n!=1])
