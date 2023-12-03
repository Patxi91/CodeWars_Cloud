def sec_deg_solver(a, b, c):
    # Check if it's a first-degree equation
    if a == 0:
        if b != 0:
            return f"It is a first degree equation. Solution: {round(-c/b, 10) if round(-c/b, 10) != -0.0 else 0.0}"
        elif c == 0:
            return "The equation is indeterminate"
        else:
            return "Impossible situation. Wrong entries"
    else:
        # Calculate the discriminant
        delta = b**2 - 4*a*c

        # Check different cases based on discriminant
        if delta < 0:
            return "There are no real solutions"
        elif delta == 0:
            solution = round((-b + delta**0.5) / (2*a), 10)
            return f"It has one double solution: {solution}"
        else:
            sol1 = round((-b + delta**0.5) / (2*a), 10)
            sol2 = round((-b - delta**0.5) / (2*a), 10)
            return f"Two solutions: {min(sol1, sol2)}, {max(sol1, sol2)}"
