
class Stack:

    def __init__(self, limit: int = 10):
        self.stack = []
        self.limit = limit

    def __bool__(self) -> bool:
        return bool(self.stack)

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, data):
        """ Push an element to the top of the stack."""
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        """ Pop an element off of the top of the stack."""
        return self.stack.pop()

    def peek(self):
        """ Peek at the top-most element of the stack."""
        return self.stack[-1]

    def is_empty(self) -> bool:
        """ Check if a stack is empty."""
        return not bool(self.stack)

    def is_full(self) -> bool:
        return self.size() == self.limit

    def size(self) -> int:
        """ Return the size of the stack."""
        return len(self.stack)

    def __contains__(self, item) -> bool:
        """Check if item is in stack"""
        return item in self.stack


def balanced_parentheses(parentheses: str) -> bool:
    stack = Stack()
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}
    for bracket in parentheses:
        if bracket in bracket_pairs:
            stack.push(bracket)
        elif bracket in (")", "]", "}"):
            if stack.is_empty() or bracket_pairs[stack.pop()] != bracket:
                return False
    return stack.is_empty()


def precedence(char: str) -> int:
    return {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}.get(char, -1)


def infix_to_postfix(expression_str: str) -> str:
    if not balanced_parentheses(expression_str):
        raise ValueError("Mismatched parentheses")
    stack = Stack()
    postfix = []
    for char in expression_str:
        if char.isalpha() or char.isdigit():
            postfix.append(char)
        elif char == "(":
            stack.push(char)
        elif char == ")":
            while not stack.is_empty() and stack.peek() != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while not stack.is_empty() and precedence(char) <= precedence(stack.peek()) and char != '^':
                postfix.append(stack.pop())
            stack.push(char)
    while not stack.is_empty():
        postfix.append(stack.pop())
    return " ".join(postfix)


expression = "1^2^3"
result = infix_to_postfix(expression).replace(" ", "")
print(result)

