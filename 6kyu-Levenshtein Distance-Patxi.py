from itertools import permutations

def is_valid_time(hh, mm):
    return 0 <= hh <= 23 and 0 <= mm <= 59

def late_clock(digits):
    max_time = -1  # Initialize with an invalid time
    for perm in permutations(digits):
        hh = perm[0] * 10 + perm[1]
        mm = perm[2] * 10 + perm[3]

        if is_valid_time(hh, mm):
            current_time = hh * 60 + mm
            max_time = max(max_time, current_time)

    # Convert the max_time back to HH:MM format
    max_hh, max_mm = divmod(max_time, 60)
    return f"{max_hh:02d}:{max_mm:02d}"
