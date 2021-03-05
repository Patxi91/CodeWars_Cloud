def order_weight(strng):

    def compute_sum(num):
        return 0 if num == 0 else int(num % 10) + compute_sum(int(num / 10))

    def sum_merge_sort(arr, sums):

        if len(sums) > 1:
            mid = len(sums) // 2
            lefthalf = sums[:mid]
            righthalf = sums[mid:]
            lefthalf_arr = arr[:mid]
            righthalf_arr = arr[mid:]

            sum_merge_sort(lefthalf_arr, lefthalf)
            sum_merge_sort(righthalf_arr, righthalf)

            i = 0  # left
            j = 0  # right
            k = 0  # Merge

            # Merging
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    sums[k] = lefthalf[i]
                    arr[k] = lefthalf_arr[i]
                    i += 1
                elif lefthalf[i] == righthalf[j]:
                    if str(lefthalf_arr[i]) < str(righthalf_arr[j]):
                        sums[k] = lefthalf[i]
                        arr[k] = lefthalf_arr[i]
                        i += 1
                    else:
                        sums[k] = righthalf[j]
                        arr[k] = righthalf_arr[j]
                        j += 1
                else:
                    sums[k] = righthalf[j]
                    arr[k] = righthalf_arr[j]
                    j += 1
                k += 1

            while i < len(lefthalf):
                sums[k] = lefthalf[i]
                arr[k] = lefthalf_arr[i]
                i += 1
                k += 1

            while j < len(righthalf):
                sums[k] = righthalf[j]
                arr[k] = righthalf_arr[j]
                j += 1
                k += 1

    arr = [int(x) for x in strng.split()]
    sums = [compute_sum(x) for x in arr]

    sum_merge_sort(arr, sums)
    return ' '.join([str(x) for x in arr])
