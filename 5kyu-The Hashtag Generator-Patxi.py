def generate_hashtag(s):
    return '#'+''.join([word.capitalize() for word in s.split()]) if s and len(s) <= 140 else False
