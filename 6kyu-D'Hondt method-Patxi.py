def distribute_seats(num_seats: int, votes: tuple[int, ...]) -> list[int]:
    num_parties = len(votes)
    seats = [0] * num_parties
    divisors = [1] * num_parties

    for i in range(num_seats):
        quotients = [votes[j] / divisors[j] for j in range(num_parties)]
        max_idx = quotients.index(max(quotients))
        seats[max_idx] += 1
        divisors[max_idx] += 1

    return seats
