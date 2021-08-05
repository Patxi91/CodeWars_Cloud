def pick_peaks(arr):
    pos = []
    peaks = []
    for i in range(1, len(arr)):
        h_next_different = next((h for h in arr[i:] if h != arr[i]), 2147483647)
        if arr[i - 1] < arr[i] and h_next_different < arr[i]:
            pos.append(i)
            peaks.append(arr[i])
    return {'pos': pos, 'peaks': peaks}
