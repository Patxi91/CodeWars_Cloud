import itertools

def mastermind(game):
    colours = ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"]
    amount = {"Red": 0, "Blue": 0, "Green": 0, "Orange": 0, "Purple": 0, "Yellow": 0, "": 0}
    guess = []
    for colour in colours:
        answer = game.check([colour, colour, colour, colour])
        colour_amount = answer.count("Black")
        amount[colour] = colour_amount
        for a in range(0,colour_amount):
            guess.append(colour)
    answer = False
    perm = list(itertools.permutations(guess, 4))
    while answer != "WON!" and answer != "Error":
        answer = game.check(list(perm.pop(0)))
