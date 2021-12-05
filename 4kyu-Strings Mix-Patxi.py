def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))
