def premier_league_standings(teams):
    # Find the team that finished first last season
    first_place_team = teams[1]

    # Remove the first place team from the dictionary
    del teams[1]

    # Sort the remaining teams alphabetically by their names
    sorted_teams = sorted(teams.values())

    # Create a new dictionary with the updated standings
    new_standings = {1: first_place_team}

    # Assign positions to the remaining teams
    for position, team in enumerate(sorted_teams, start=2):
        new_standings[position] = team

    return new_standings
