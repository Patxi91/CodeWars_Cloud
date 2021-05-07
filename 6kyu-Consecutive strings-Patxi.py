
def longest_consec(strarr, k):

    if not strarr or k <= 0 or k >= len(strarr):
        return ''
    else:

        s = 0  # Sum
        m = 0  # Max

        for i in range(len(strarr)-(k-1)):
            s = len(''.join(strarr[i: i+k]))
            if s > m:
                m = s
                sub_strarr = ''.join(strarr[i: i+k])
            s = 0

    return sub_strarr
