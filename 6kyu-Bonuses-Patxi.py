def bonus(arr, s):
    s=s/(sum(1/n for n in arr))
    return [round(s/n) for n in arr]
