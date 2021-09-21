def binarray(s) -> int:
    hash_map = {}
    curr_sum = 0
    max_len = 0
    ending_index = -1
    n = len(s)

    for i in range(0, n):
        if (s[i] == 0):
            s[i] = -1
        else:
            s[i] = 1

    # Traverse through the given array
    for i in range(0, n):
        # Add current element to sum
        curr_sum = curr_sum + s[i]

        # To handle sum = 0 at last index
        if (curr_sum == 0):
            max_len = i + 1
            ending_index = i

        # If this sum is seen before,
        if curr_sum in hash_map:

            # If max_len is smaller than new subarray
            # Update max_len and ending_index
            if max_len < i - hash_map[curr_sum]:
                max_len = i - hash_map[curr_sum]
                ending_index = i
        else:
            # else put this sum in dictionary
            hash_map[curr_sum] = i

    for i in range(0, n):
        if (s[i] == -1):
            s[i] = 0
        else:
            s[i] = 1

    return max_len if max_len != -1 else 0
