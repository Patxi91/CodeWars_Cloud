def child(bird1, bird2):
    if bird1 == bird2:
        return False
    return get_difference(bird1, bird2) < 3


def grandchild(bird1, bird2):
    if len(bird1) == 1 and len(bird2) == 1 and bird1 != bird2:
        return False
    return get_difference(bird1, bird2) <= 4


def get_difference(bird1, bird2):
    diff_count = 0
    for i in range(len(bird1)):
        if bird1[i] != bird2[i]:
            diff_count += 1
    return diff_count
