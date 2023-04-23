def find_hack(arr):
    hacked_entries = []
    for record in arr:
        total_points = 0
        for grade in record[2]:
            if grade == "A":
                total_points += 30
            elif grade == "B":
                total_points += 20
            elif grade == "C":
                total_points += 10
            elif grade == "D":
                total_points += 5
        if len(record[2]) >= 5 and all(grade in ["A", "B"] for grade in record[2]):
            total_points += 20
        total_points = min(total_points, 200)
        if total_points != record[1]:
            hacked_entries.append(record[0])
    return hacked_entries
