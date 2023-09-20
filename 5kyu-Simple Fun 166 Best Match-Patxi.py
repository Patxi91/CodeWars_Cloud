def best_match(ALAHLYGoals, zamalekGoals):
    best_index = 0  # Initialize the index of the best match to the first match
    min_goal_difference = ALAHLYGoals[0] - zamalekGoals[0]

    for i in range(1, len(ALAHLYGoals)):
        goal_difference = ALAHLYGoals[i] - zamalekGoals[i]

        # Check if the current match has a smaller goal difference or
        # the same goal difference but more goals scored by Zamalek
        if goal_difference < min_goal_difference or (
            goal_difference == min_goal_difference and zamalekGoals[i] > zamalekGoals[best_index]
        ):
            best_index = i
            min_goal_difference = goal_difference

    return best_index
