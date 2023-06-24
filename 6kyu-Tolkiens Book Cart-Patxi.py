from collections import Counter

def calculate_cart_total(contents):
    book_prices = 10  # Price of each book
    discounts = [0, 0.05, 0.1, 0.2]  # Discounts based on the number of different titles

    # Count the number of occurrences for each title
    title_counts = Counter(contents)

    # Sort the title counts in descending order
    sorted_counts = sorted(title_counts.values(), reverse=True)

    # Calculate the total cost
    total_cost = 0
    while sorted_counts:
        num_titles = len(sorted_counts)
        discount = discounts[num_titles - 1]  # Get the applicable discount
        total_cost += num_titles * book_prices * (1 - discount)
        sorted_counts = [count - 1 for count in sorted_counts if count > 1]

    return total_cost
