def increment_string(strng):
    s_dig = ''
    s_alp = ''

    for i in range(len(strng), 0, -1):
        if strng[i - 1].isdigit():
            s_dig += strng[i - 1]
        else:
            s_alp += strng[0:i]
            break
    s_dig = s_dig[::-1]
    if (len(s_dig) == 0):
        strng += str(1)
        return strng
    else:
        num = int(s_dig)
        num += 1
        num_s = str(num)
        for i in range(len(s_dig) - len(num_s)):
            num_s = ''.join(('0', num_s))
        strng = s_alp + num_s
        return strng