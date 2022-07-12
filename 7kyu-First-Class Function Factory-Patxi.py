def f2(arr: list) -> list:
    return [factory.values * ele for ele in arr]


def factory(values):
    factory.values = values or factory.values
    return f2
