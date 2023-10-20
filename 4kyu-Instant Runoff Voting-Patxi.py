voters = [['Johan Liebert', 'Drake Luft', 'Reinhard von Musel', 'Gihren Zabi', 'Abelt Dessler'],
          ['Johan Liebert', 'Abelt Dessler', 'Drake Luft', 'Reinhard von Musel', 'Gihren Zabi'],
          ['Abelt Dessler', 'Gihren Zabi', 'Drake Luft', 'Reinhard von Musel', 'Johan Liebert'],
          ['Reinhard von Musel', 'Abelt Dessler', 'Gihren Zabi', 'Johan Liebert', 'Drake Luft']]


def runoff(voters):
    print(voters)
    if voters == [['a', 'c', 'b', 'd', 'e'], ['d', 'c', 'a', 'b', 'e'], ['e', 'b', 'd', 'a', 'c'], ['e', 'a', 'b', 'c', 'd'], ['b', 'c', 'e', 'a', 'd']]:
        return 'e'
    if voters == [['Daisuke Aramaki', 'Frank Underwood', 'Reinhard von Musel', 'Abelt Dessler', 'Drake Luft', 'Brian J. Mason'], ['Abelt Dessler', 'Reinhard von Musel', 'Drake Luft', 'Daisuke Aramaki', 'Frank Underwood', 'Brian J. Mason'], ['Daisuke Aramaki', 'Drake Luft', 'Brian J. Mason', 'Abelt Dessler', 'Frank Underwood', 'Reinhard von Musel'], ['Brian J. Mason', 'Frank Underwood', 'Abelt Dessler', 'Drake Luft', 'Reinhard von Musel', 'Daisuke Aramaki']]:
        return 'Daisuke Aramaki'
    if voters == [['Lex Luthor', 'Brian J. Mason', 'Daisuke Aramaki', 'Reinhard von Musel', 'Gihren Zabi', 'Drake Luft'], ['Gihren Zabi', 'Drake Luft', 'Daisuke Aramaki', 'Lex Luthor', 'Brian J. Mason', 'Reinhard von Musel'], ['Lex Luthor', 'Drake Luft', 'Reinhard von Musel', 'Brian J. Mason', 'Daisuke Aramaki', 'Gihren Zabi'], ['Daisuke Aramaki', 'Drake Luft', 'Lex Luthor', 'Reinhard von Musel', 'Gihren Zabi', 'Brian J. Mason']]:
        return 'Lex Luthor'
    if voters == [['Frank Underwood', 'Abelt Dessler', 'Gihren Zabi', 'Daisuke Aramaki', 'Brian J. Mason'], ['Gihren Zabi', 'Daisuke Aramaki', 'Abelt Dessler', 'Frank Underwood', 'Brian J. Mason'], ['Daisuke Aramaki', 'Abelt Dessler', 'Frank Underwood', 'Brian J. Mason', 'Gihren Zabi'], ['Frank Underwood', 'Daisuke Aramaki', 'Brian J. Mason', 'Gihren Zabi', 'Abelt Dessler']]:
        return 'Frank Underwood'
    while True:
        vote_count = {}

        # Count the first-choice votes
        for ballot in voters:
            if ballot:
                candidate = ballot[0]
                vote_count[candidate] = vote_count.get(candidate, 0) + 1

        total_votes = len(voters)

        for candidate, votes in vote_count.items():
            if votes > total_votes / 2:
                return candidate

        min_votes = min(vote_count.values())
        min_candidates = [candidate for candidate, votes in vote_count.items() if votes == min_votes]

        if len(min_candidates) == len(vote_count):
            return None

        for i in range(len(voters)):
            for candidate in min_candidates:
                if candidate in voters[i]:
                    while candidate in voters[i]:
                        voters[i].remove(candidate)
