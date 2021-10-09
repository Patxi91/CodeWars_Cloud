# Create objects of the values of good, evil, and result messages
good = {
    0: 1,
    1: 2,
    2: 3,
    3: 3,
    4: 4,
    5: 10
}

evil = {
    0: 1,
    1: 2,
    2: 2,
    3: 2,
    4: 3,
    5: 5,
    6: 10
}

results = {
    "good": "Battle Result: Good triumphs over Evil",
    "evil": "Battle Result: Evil eradicates all trace of Good",
    "draw": "Battle Result: No victor on this battle field"
}


# Convert the string input into a list of values
def listify(s):
    s = [int(i) for i in s.split(" ")]
    return s


# Solution
def good_vs_evil(team_good, team_evil):
    team_good = listify(team_good)
    team_evil = listify(team_evil)

    score_good = 0
    score_evil = 0

    for i in range(len(team_good)):
        score_good += team_good[i] * good[i]

    for i in range(len(team_evil)):
        score_evil += team_evil[i] * evil[i]

    if score_good > score_evil:
        return results["good"]
    elif score_evil > score_good:
        return results["evil"]
    else:
        return results["draw"]
