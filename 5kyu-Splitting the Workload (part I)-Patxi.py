def split_list(xs):
    n = len(xs)
    min_diff = float('inf')  # Initialize with infinity
    best_partition = None

    # Generate all possible partitions of the jobs
    for i in range(2 ** n):
        partition_a = []
        partition_b = []
        for j in range(n):
            if (i >> j) & 1:
                partition_a.append(xs[j])
            else:
                partition_b.append(xs[j])

        # Calculate the absolute difference between the sums
        diff = abs(sum(partition_a) - sum(partition_b))

        # Update the minimum difference and best partition if necessary
        if diff < min_diff:
            min_diff = diff
            best_partition = (partition_a, partition_b)

    return best_partition
