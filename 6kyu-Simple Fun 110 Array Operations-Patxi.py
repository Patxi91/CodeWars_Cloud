def array_operations(a, k):

    remaining_iterations = 1 if k % 2 else 2

    while remaining_iterations > 0:
        # Find the highest value in the list
        max_value = max(a)

        # Apply the operation to each element using map and a lambda function
        a = list(map(lambda element: max_value - element, a))

        # Decrement the remaining iterations
        remaining_iterations -= 1

    # Return the modified list
    return a
