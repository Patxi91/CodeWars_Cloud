def womens_age(age):
    base_value = age // 2
    remainder_value = age % 2
    return "{}? That's just {}, in base {}!".format(age, 20 + remainder_value, base_value)
