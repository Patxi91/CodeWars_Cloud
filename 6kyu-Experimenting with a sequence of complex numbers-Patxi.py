import cmath

def f(z, eps):
    n = 1
    prev_sum = 0
    term = z
    max_iterations = 10000  # Maximum number of iterations to avoid infinite loops
    while n <= max_iterations:
        current_sum = prev_sum + term
        if n > 1 and abs(current_sum - prev_sum) < eps:
            return n
        prev_sum = current_sum
        term *= z
        n += 1
    return -1  # If the loop exceeds the maximum iterations, return -1
