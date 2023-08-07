from typing import List, Tuple
from preloaded import visualize_polygon

def point_in_polygon(polygon: List[Tuple[float, float]], point: Tuple[float, float]) -> bool:
    x, y = point
    num_vertices = len(polygon)
    odd_nodes = False

    j = num_vertices - 1
    for i in range(num_vertices):
        xi, yi = polygon[i]
        xj, yj = polygon[j]

        if (yi < y and yj >= y) or (yj < y and yi >= y):
            if xi + (y - yi) / (yj - yi) * (xj - xi) < x:
                odd_nodes = not odd_nodes
        j = i

    return odd_nodes
