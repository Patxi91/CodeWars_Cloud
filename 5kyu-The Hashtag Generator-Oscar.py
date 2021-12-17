def generate_hashtag(s):

    return False if not len(s) else False if len('#'+''.join(word[0].upper()+word[1:].lower() for word in s.split() )) > 140 else '#'+''.join(word[0].upper()+word[1:].lower() for word in s.split()) 



print(generate_hashtag('codewars is nice'))