def odd(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'o':
            for j in range(i+1, len(s)):
                if s[j] == 'd':
                    for k in range(j+1, len(s)):
                        if s[k] == 'd':
                            count += 1
                            s = s[:i] + '.' + s[i+1:j] + '.' + s[j+1:k] + '.' + s[k+1:]
                            break
                    break
    return count
