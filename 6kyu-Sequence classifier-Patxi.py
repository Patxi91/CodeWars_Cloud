def sequence_classifier(arr):
    diffs = [b - a for a, b in zip(arr, arr[1:])]
    if all(d == 0 for d in diffs):
        return 5
    elif all(d > 0 for d in diffs):
        return 1
    elif all(d >= 0 for d in diffs):
        return 2
    elif all(d < 0 for d in diffs):
        return 3
    elif all(d <= 0 for d in diffs):
        return 4
    else:
        return 0
