def create_two_sets_of_equal_sum(n):
    total_sum = (n * (n + 1)) // 2  # Calculate the sum of all integers from 1 to n

    if total_sum % 2 != 0:
        return []  # Return an empty list if the total sum is not even

    target_sum = total_sum // 2  # Calculate the target sum for each set

    set1 = []  # First set
    set2 = []  # Second set

    for i in range(n, 0, -1):
        if i <= target_sum:
            set1.append(i)
            target_sum -= i
        else:
            set2.append(i)

    return set1, set2
