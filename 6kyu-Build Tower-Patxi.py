def tower_builder(n_floors):
    return [('*' + '*' * i * 2).center(1 + 2 * (n_floors - 1)) for i in range(n_floors)]
