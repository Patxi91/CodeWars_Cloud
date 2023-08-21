def max_overlap(img1, img2):
    n = len(img1)  # Number of rows
    m = len(img1[0])  # Number of columns

    max_overlap = 0

    # Iterate through all possible shifts
    for shift_i in range(-n + 1, n):
        for shift_j in range(-m + 1, m):
            overlap_count = 0

            # Iterate through the pixels of both images
            for i in range(n):
                for j in range(m):
                    # Calculate the corresponding indices after shifting
                    img1_i = i + shift_i
                    img1_j = j + shift_j

                    # Check if both indices are within bounds
                    if 0 <= img1_i < n and 0 <= img1_j < m:
                        # Check if both pixels are black
                        if img1[img1_i][img1_j] == 1 and img2[i][j] == 1:
                            overlap_count += 1

            # Update max_overlap if current overlap is greater
            max_overlap = max(max_overlap, overlap_count)

    return max_overlap
