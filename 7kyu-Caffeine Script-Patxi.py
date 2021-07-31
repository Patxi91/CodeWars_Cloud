def caffeine_buzz(n):
    return 'CoffeeScript' if n % 12 == 0 else 'JavaScript' if n % 6 == 0 else 'Java' if n % 3 == 0 else 'mocha_missing!'
