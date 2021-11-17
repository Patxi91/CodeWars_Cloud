def uncensor(infected, discovered):
    return infected.replace('*', '{}').format(*discovered)
