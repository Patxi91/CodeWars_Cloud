def valid_parentheses(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        elif i in ')':
            if len(stack) > 0 and '(' == stack[len(stack)-1]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
