def solve(st):
    stack = []
    current_string = ""
    repeat_count = 1

    for char in st:
        if char.isdigit():
            repeat_count = int(char)
        elif char.isalpha():
            current_string += char
        elif char == "(":
            stack.append((current_string, repeat_count))
            current_string = ""
            repeat_count = 1
        elif char == ")":
            prev_string, prev_repeat = stack.pop()
            current_string = prev_string + current_string * prev_repeat

    return current_string
