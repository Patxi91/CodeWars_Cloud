def letter_pattern(words):
    if len(words) == 1:
        return words[0]
    else:
        ans = []
        i = 0
        while i < len(words[0]):
            sample = words[0][i]

            j = 1
            c = 1

            while j < len(words):
                if sample != words[j][i]:
                    c = 0
                    ans.append('*')
                    break
                j += 1

            if c:
                ans.append(sample)

            i += 1
        return ''.join(ans)
