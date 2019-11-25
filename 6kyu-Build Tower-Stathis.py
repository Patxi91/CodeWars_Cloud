def tower_builder(n_floors):
    tower = ['{0}{1}{0}'.format(' ' * (((n_floors*2-1)-(i*2+1))//2), '*' * (i * 2 + 1)) for i in range(n_floors)]
    return tower   
