def same_case(a, b):
    return (a.isupper() == b.isupper() or a.islower() == b.islower()) if (a.isalpha() and b.isalpha()) else -1
