def baby_shark_lyrics():
    shks = ['Baby shark', 'Mommy shark', 'Daddy shark', 'Grandma shark', 'Grandpa shark', 'Let\'s go hunt']
    output = ''
    for s in shks:
        output += (s + ',' + ' doo'*6 + '\n')*3 + s + '!\n'
    return output + 'Run away,…'
