def initials(name):
    # Split the full name into parts by space
    parts = name.split()

    # Initialize an empty list to store the initials
    initials_list = []

    # Iterate through the parts, excluding the last one
    for part in parts[:-1]:
        # Take the first character of each part and capitalize it
        initials_list.append(part[0].upper())

    # Add the last name with its first letter capitalized
    last_name = parts[-1].capitalize()

    # Combine the initials and the last name with dots
    result = '.'.join(initials_list + [last_name])

    return result
