def get_middle(s):
    if len(s) % 2 == 0:#isEVEN
        return s[int(len(s)/2) -1:int(len(s)/2) +1]
    else:#isODD
        return s[int((len(s)-1) /2)]
