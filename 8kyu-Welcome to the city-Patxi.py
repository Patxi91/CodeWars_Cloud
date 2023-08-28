def say_hello(name, city, state):
    full_name = ' '.join(name)  # Join the name parts with a space
    welcome_message = f"Hello, {full_name}! Welcome to {city}, {state}!"
    return welcome_message
