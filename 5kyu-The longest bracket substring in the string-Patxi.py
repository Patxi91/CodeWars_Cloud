def find_longest(st):
    stack = []  # Stack to track the indices of "(" characters
    max_length = 0  # Variable to store the maximum substring length
    start = -1  # Start index of the current substring

    for i, char in enumerate(st):
        if char == "(":
            stack.append(i)  # Push the index of "(" character to the stack
            if start == -1:
                start = i  # Update the start index of the current substring

        elif char == ")":
            if stack:  # If stack is not empty
                stack.pop()  # Pop the top "(" from the stack

                if stack:
                    length = i - stack[-1]  # Calculate the current substring length
                    max_length = max(max_length, length)  # Update the maximum substring length
                else:
                    length = i - start + 1  # Calculate the current substring length including all ")"
                    max_length = max(max_length, length)  # Update the maximum substring length

            else:
                start = -1  # Reset the start index if the current ")" does not have a matching "("

    return max_length
