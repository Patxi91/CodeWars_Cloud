from typing import List
from collections import deque

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Function to find all four-digit prime numbers
def find_four_digit_primes():
    primes = []
    for num in range(1000, 10000):
        if is_prime(num):
            primes.append(num)
    return primes

# Function to find the neighbors (valid prime numbers) of a given number
def find_neighbors(num, primes):
    neighbors = []
    num_str = str(num)
    for i in range(4):
        for j in range(10):
            if i == 0 and j == 0:
                continue  # Avoid leading zeros
            new_num_str = num_str[:i] + str(j) + num_str[i+1:]
            new_num = int(new_num_str)
            if new_num in primes and new_num != num:
                neighbors.append(new_num)
    return neighbors

def find_shortest_path(start: int, end: int) -> List[int]:
    if start == end:
        return [start]

    primes = set(find_four_digit_primes())

    if start not in primes or end not in primes:
        return []

    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        for neighbor in find_neighbors(current, primes):
            if neighbor == end:
                return path + [end]
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return []
