spoken = lambda greeting: greeting.capitalize() + '.'

shouted = lambda greeting: greeting.upper() + '!'

whispered = lambda greeting: greeting.lower() + '.'

greet = lambda style, msg: style(msg)
