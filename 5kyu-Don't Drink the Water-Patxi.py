def separate_liquids(glass):
    if not glass:
        return []

    density_chart = {
        'H': 1.36,
        'W': 1.00,
        'A': 0.87,
        'O': 0.80
    }

    rows, cols = len(glass), len(glass[0])
    liquids = []
    for row in glass:
        liquids.extend(row)

    liquids.sort(key=lambda x: density_chart.get(x))

    sorted_glass = [liquids[i:i+cols] for i in range(0, rows*cols, cols)]

    return sorted_glass
