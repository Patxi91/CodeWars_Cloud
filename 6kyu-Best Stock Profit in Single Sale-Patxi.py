def max_profit(prices):
    max_profit = float("-inf")
    minimum_num = float("inf")

    for num in prices:
        if num < minimum_num:
            max_profit = max(max_profit, num - minimum_num)
            minimum_num = num
            continue
        max_profit = max(max_profit, num - minimum_num)
    return max_profit
