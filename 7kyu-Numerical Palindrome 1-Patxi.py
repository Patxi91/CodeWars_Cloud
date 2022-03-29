def palindrome(num):
    if isinstance(num, int) and num >= 0:
        return num == int(str(num)[::-1])
    else:
        return "Not valid"
