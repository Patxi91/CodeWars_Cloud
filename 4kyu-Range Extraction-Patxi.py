import re


def solution(args):
    statement = ''

    diffs = [args[i] - args[i - 1] for i in range(1, len(args))]
    diffs.insert(0, 0)

    diffs = ''.join([str(i) for i in diffs])

    matches = []

    def repl(m):
        matches.append(m.group())
        return ("+" * len(m.group()[:-2])).format(m.group()[:-2]) + "-e"

    pattern = re.compile(r"1[1+]*1")
    diffs = re.sub(pattern, repl, diffs)

    for i in range(len(diffs)):
        if diffs[i] == "+":
            continue
        elif diffs[i] == "-":
            statement += "-" + str(args[i + 1]) + ","
        else:
            statement += "," + str(args[i])

    statement = re.sub(",,-*\d+", "", statement[1:])

    return statement
