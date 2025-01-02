#Path Finder #1: can you reach the exit?
import numpy as np
from queue import Queue

def path_finder(maze):
    maze = [list(row) for row in maze.split("\n")]
    maze = np.array(maze)
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    start = (0,0)
    end = (maze.shape[0]-1, maze.shape[1]-1)
    if start == end:
        return 0
    visited = np.zeros_like(maze, dtype=bool)
    visited[start] = True
    queue = Queue()
    queue.put((start, []))
    while not queue.empty():
        (node, path) = queue.get()
        for dx, dy in directions:
            next_node = (node[0]+dx, node[1]+dy)
            if (next_node == end):
                return len(path)+1
            if (next_node[0] >= 0 and next_node[1] >= 0 and 
                next_node[0] < maze.shape[0] and next_node[1] < maze.shape[1] and 
                maze[next_node] == "." and not visited[next_node]):
                visited[next_node] = True
                queue.put((next_node, path + [next_node]))
    return False

    #return True # can go to lower right corner from upper left one



maze2 = "\n".join([
    "....W.",
    "..W...",
    "WW....",
    "......",
    "......",
    "......"
])
print(maze2)

print(path_finder(maze2))