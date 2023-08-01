def increasing_numbers(digits):
    if digits == 0:
        return 1

    # Create a table to store the count of non-decreasing numbers for each digit
    dp = [[0 for _ in range(10)] for _ in range(digits)]

    # Initialization: For a single digit, we have 10 non-decreasing numbers (0 to 9)
    for i in range(10):
        dp[0][i] = 1

    # Calculate the count of non-decreasing numbers for each digit
    for i in range(1, digits):
        for j in range(10):
            dp[i][j] = sum(dp[i - 1][k] for k in range(j + 1))

    result = sum(dp[digits - 1])
    return result
