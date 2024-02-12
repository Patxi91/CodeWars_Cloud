def solve(s):
    stack = []
    i = 0
    while i < len(s):
        if s[i:i+12] == '[backspace]*':
            i += 12  # Skip past '[backspace]*'
            num_start = i  # Start of the number following '*'
            while i < len(s) and s[i].isdigit():
                i += 1
            num_backspaces = int(s[num_start:i])  # Parse the number
            stack = stack[:-num_backspaces]  # Remove 'num_backspaces' elements from the stack
        elif s[i:i+11] == '[backspace]':
            stack = stack[:-1]  # Remove one element from the stack
            i += 11  # Skip past '[backspace]'
        else:
            stack.append(s[i])  # Add the character to the stack
            i += 1  # Move to the next character
    return ''.join(stack)  # Join all characters in the stack into a string
