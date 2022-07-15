def rake_garden(g):
    return ' '.join([x if x=='gravel' or x=='rock' else 'gravel' for x in g.split()])