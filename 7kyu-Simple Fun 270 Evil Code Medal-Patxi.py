def evil_code_medal(user_time, gold, silver, bronze):
    if user_time < gold:
        return "Gold"
    elif user_time < silver:
        return "Silver"
    elif user_time < bronze:
        return "Bronze"
    else:
        return "None"
