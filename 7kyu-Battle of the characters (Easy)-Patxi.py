def findTheSum(str):

    alpha = ""

    # Traverse the given string
    for i in range(0, len(str)):

        # If character is an alphabet
        if ((str[i] >= 'A' and str[i] <= 'Z') or (str[i] >= 'a' and str[i] <= 'z')):
            alpha += str[i]

    # Stores the sum of order of values
    score = 0
    n = 0

    for i in range(0, len(alpha)):

        # Find the score
        if (alpha[i] >= 'A' and alpha[i] <= 'Z'):
            score += ord(alpha[i]) - ord('A') + 1

        else:
            score += ord(alpha[i]) - ord('a') + 1

    return score


def battle(x, y):
    return x if findTheSum(x)>findTheSum(y) else y if findTheSum(y)>findTheSum(x) else "Tie!"
