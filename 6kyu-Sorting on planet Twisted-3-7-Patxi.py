def sort_twisted37(arr):
    arr = [str(n).replace("3", "/3").replace("7", "3").replace("/3", "7") for n in arr]

    arr = [int(n) for n in arr]
    arr.sort()

    arr = [str(n).replace("3", "/3").replace("7", "3").replace("/3", "7") for n in arr]

    return [int(n) for n in arr]
