import string
import os


def grid(N):
    sol = ''

    if N < 0:
        return None
    elif N == 0:
        return ''

    i = 0
    for x in range(N):
        for y in (string.ascii_lowercase * (1 + 2 * N // 26))[i:N + i]:
            sol = sol + y + ' '

        sol = sol.rstrip()
        sol += os.linesep
        i += 1
    sol = sol.rstrip('\n')
    return sol
