from collections import deque


def processes(start, end, processes):
    if start == end:
        return []

    adj_list = {}
    for process, s, e in processes:
        if s not in adj_list:
            adj_list[s] = []
        adj_list[s].append((e, process))

    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        if current not in visited:
            visited.add(current)
            if current in adj_list:
                for neighbor, process in adj_list[current]:
                    queue.append((neighbor, path + [process]))
    return []
