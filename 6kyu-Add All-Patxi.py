import heapq


def add_all(lst):
    # Create min heap
    heapq.heapify(lst)

    # Initialize total cost to 0
    total_cost = 0

    # Keep merging two smallest elements until only one element is left in the heap
    while len(lst) > 1:
        # Extract the two smallest elements
        a = heapq.heappop(lst)
        b = heapq.heappop(lst)

        # Add their sum to the total cost
        total_cost += a + b

        # Push the sum back into the heap
        heapq.heappush(lst, a + b)

    # Return the total cost
    return total_cost
