def rad_ladies(name):
    # Initialize an empty string to store the filtered name
    filtered_name = ""

    # Define a set of characters to keep (alpha characters, spaces, and exclamation marks)
    keep_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !")

    # Iterate through each character in the input name
    for char in name:
        # Check if the character is in the set of characters to keep
        if char in keep_chars:
            # Convert the character to uppercase and add it to the filtered name
            filtered_name += char.upper()

    return filtered_name

