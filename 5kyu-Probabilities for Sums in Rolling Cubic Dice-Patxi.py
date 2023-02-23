def rolldice_sum_prob(sum_, dice_amount):
    def count_ways(sum_, dice_amount):
        # Base case: we have rolled all the dice
        if dice_amount == 0:
            return 1 if sum_ == 0 else 0

        # Recursive case: consider all possible outcomes for the first die
        # and recursively calculate the number of ways to get the remaining sum
        count = 0
        for i in range(1, 7):
            count += count_ways(sum_ - i, dice_amount - 1)

        return count

    total_ways = 6 ** dice_amount  # Total number of possible outcomes
    desired_ways = count_ways(sum_, dice_amount)  # Number of ways to get the desired sum

    return desired_ways / total_ways  # Probability of getting the desired sum
