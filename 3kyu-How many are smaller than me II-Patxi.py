def smaller(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        merged = []
        count = 0
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                merged.append(left[i])
                result[left[i][1]] += count
                i += 1
            else:
                merged.append(right[j])
                count += 1
                j += 1

        while i < len(left):
            merged.append(left[i])
            result[left[i][1]] += count
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    result = [0] * len(arr)
    arr = [(num, index) for index, num in enumerate(arr)]
    merge_sort(arr)
    return result
