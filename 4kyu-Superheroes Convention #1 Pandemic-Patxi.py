def is_possible(database: dict) -> bool:
    # create graph
    graph = {superhero: set(hates) for superhero, hates in database.items()}
    # initialize color map
    colors = {superhero: 0 for superhero in graph}

    def dfs(superhero, color):
        colors[superhero] = color
        for neighbor in graph[superhero]:
            if colors[neighbor] == color:
                return False
            if colors[neighbor] == 0 and not dfs(neighbor, 3 - color):
                return False
        return True

    # traverse graph with DFS
    for superhero in graph:
        if colors[superhero] == 0 and not dfs(superhero, 1):
            return False
    return True
