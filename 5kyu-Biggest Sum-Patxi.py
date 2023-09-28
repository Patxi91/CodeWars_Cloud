def find_sum(m):
    size = len(m)

    # Create a table to store the maximum sum for each cell
    dp = [[0] * size for _ in range(size)]

    # Initialize the first row and first column of the table
    dp[0][0] = m[0][0]
    for i in range(1, size):
        dp[i][0] = dp[i - 1][0] + m[i][0]
        dp[0][i] = dp[0][i - 1] + m[0][i]

    # Fill the rest of the table using dynamic programming
    for i in range(1, size):
        for j in range(1, size):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + m[i][j]

    # The bottom-right corner of the table contains the maximum sum
    return dp[size - 1][size - 1]
