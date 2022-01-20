class Automaton(object):

    def __init__(self):
        self.states = []

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        s = 1
        for x in commands:
            if s == 1:
                if x == "1":
                    s = 2
            elif s == 2:
                if x == "0":
                    s = 3
            else:
                s = 2

        return s == 2


my_automaton = Automaton()

# Do anything necessary to set up your automaton's states, q1, q2, and q3.
