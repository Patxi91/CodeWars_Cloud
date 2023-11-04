def win_round(you, opp):
    your_max_number = int(''.join(map(str, sorted(you, reverse=True)[:2])))
    opp_max_number = int(''.join(map(str, sorted(opp, reverse=True)[:2])))

    return your_max_number > opp_max_number
