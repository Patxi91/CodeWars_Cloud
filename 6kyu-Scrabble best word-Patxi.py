def get_best_word(points, words):
    # Create a dictionary to map letters to their corresponding points
    letter_points = {chr(i + 65): points[i] for i in range(26)}

    # Initialize variables to keep track of the best word
    best_score = 0
    best_length = float('inf')
    best_index = -1

    # Iterate over all words
    for i, word in enumerate(words):
        # Calculate the score of the current word
        score = sum(letter_points[letter] for letter in word)
        length = len(word)

        # Update the best word if the current word has a higher score or
        # if it has the same score but a shorter length
        if score > best_score or (score == best_score and length < best_length):
            best_score = score
            best_length = length
            best_index = i

    return best_index
