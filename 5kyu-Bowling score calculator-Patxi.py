def bowling_score(rolls):
    total_score, current_roll, current_frame = 0, 0, 0

    while current_roll < len(rolls):
        if current_frame == 10:
            break

        if rolls[current_roll] == 10 and current_roll < len(rolls) - 2:
            total_score += 10 + rolls[current_roll + 1] + rolls[current_roll + 2]
        elif rolls[current_roll] + rolls[current_roll + 1] == 10:
            total_score += 10 + rolls[current_roll + 2]
            current_roll += 1
        else:
            total_score += rolls[current_roll] + rolls[current_roll + 1]
            current_roll += 1

        current_roll += 1
        current_frame += 1

    return total_score
