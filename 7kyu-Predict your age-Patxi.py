def predict_age(*ages):
    return (sum([age**2 for age in ages]) ** (1/2)) // 2
