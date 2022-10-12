def assemble(arr):
    if not arr:
        return ''
    r = ["#"]*len(arr[0])
    for s in arr:
        for i in range(len(s)):
            if s[i] != "*":
                r[i] = s[i]
    return "".join(r)
