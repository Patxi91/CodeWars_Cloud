def consecutive_ducks(n):
    def canBeSumofConsec(n):

        # We basically return true if n is a
        # power of two
        return ((n & (n - 1)) and n)

        # Driver code

    if (canBeSumofConsec(n)):
        return True
    else:
        return False