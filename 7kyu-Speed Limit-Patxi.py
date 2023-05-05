def speed_limit(speed, signals):
    fine = 0
    for signal in signals:
        overspeed = speed - signal
        if overspeed >= 30:
            fine += 500
        elif overspeed >= 20:
            fine += 250
        elif overspeed >= 10:
            fine += 100
    return fine
