def replace_last(string, find, replace):
    reversed = string[::-1]
    replaced = reversed.replace(find[::-1], replace[::-1], 1)
    return replaced[::-1]


def format_duration(seconds):

    TIME_DURATION_UNITS = (
        ('year', 60 * 60 * 24 * 365),
        ('day', 60 * 60 * 24),
        ('hour', 60 * 60),
        ('minute', 60),
        ('second', 1))

    if seconds == 0:
        return 'now'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'.format(amount, unit, "" if amount == 1 else "s"))
    result = ', '.join(parts)
    result = replace_last(result, ",", " and")
    return result

