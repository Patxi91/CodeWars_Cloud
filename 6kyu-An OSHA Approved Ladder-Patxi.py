def is_ladder_safe(ldr):
    # Find the positions of rungs in each row
    rung_positions = []
    for row in ldr:
        rungs = [i for i, char in enumerate(row) if char == "#"]
        rung_positions.append(rungs)

    # Check the first and last rung positions
    if len(rung_positions[0]) != 2 or len(rung_positions[-1]) != 2:
        return False
    # Check that the second and second to last rungs have length >= 5
    if len(rung_positions[1]) < 5 or len(rung_positions[-2]) < 5:
        return False

    # Check if any row in the ladder is less than 5 characters wide
    if any(len(row) < 5 for row in ldr):
        return False

    # The ladder mustn't have more than a 2 character gap between rungs
    # There should be at least one rung
    # Rungs must be evenly spaced apart
    consecutive_gap_count = 0  # Figure max gap
    max_consecutive_gap = 1e6  # Maximum
    has_at_least_one_rung = False
    for positions in rung_positions:
        if len(positions) >= 5:
            if has_at_least_one_rung:
                max_consecutive_gap = consecutive_gap_count
                has_at_least_one_rung = False
                break
            has_at_least_one_rung = True
            consecutive_gap_count = 0
        elif len(positions) == 2:
            consecutive_gap_count += 1
            if consecutive_gap_count > 2:
                return False
    consecutive_gap_count = 0
    has_at_least_one_rung = False
    length_2_counts = []
    if max_consecutive_gap == 1e6:  # When there is 0 gaps
        max_consecutive_gap = 0
    for positions in rung_positions:
        if len(positions) >= 5:
            if consecutive_gap_count != max_consecutive_gap and has_at_least_one_rung:
                return False
            has_at_least_one_rung = True
            consecutive_gap_count = 0
        elif len(positions) == 2:
            consecutive_gap_count += 1
            length_2_counts.append(len(positions))
        else:
            return False
    if not has_at_least_one_rung or not (len(set(length_2_counts)) == 1 and length_2_counts[0] >= 2):
        return False

    # Check if each part of the ladder has equal width
    ladder_width = len(ldr[0])
    if any(len(row) != ladder_width for row in ldr):
        return False

    # Check if rungs are not broken
    for positions in rung_positions:
        if len(positions) >= 5:
            for i in range(1, len(positions)):
                if positions[i] - positions[i - 1] != 1:
                    return False

    return True
