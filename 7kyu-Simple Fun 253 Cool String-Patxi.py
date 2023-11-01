def cool_string(s):
    if not s or not s.isalpha():
        return False  # If the string is empty or contains non-alphabetic characters, it's not cool.

    for i in range(1, len(s)):
        if (s[i - 1].islower() and s[i].islower()) or (s[i - 1].isupper() and s[i].isupper()):
            return False  # Two lowercase or two uppercase letters in adjacent positions, not cool.

    return True
