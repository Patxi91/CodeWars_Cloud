def subsequence_sums(arr, s):
    count = 0
    cumulative_sum = 0
    sum_freq = {0: 1}  # Dictionary to store frequencies of cumulative sums

    for num in arr:
        cumulative_sum += num
        if cumulative_sum - s in sum_freq:
            count += sum_freq[cumulative_sum - s]
        if cumulative_sum in sum_freq:
            sum_freq[cumulative_sum] += 1
        else:
            sum_freq[cumulative_sum] = 1

    return count
