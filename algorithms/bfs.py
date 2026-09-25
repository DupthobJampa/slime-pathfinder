from collections import deque

def bfs(grid, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {}

    directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]
    while queue:
        current = queue.popleft()
        row, col = current
        if current == goal:
            path = []
            while (current != start):
                path.append(current)
                current = parent[current]
            path.append(current)
            path.reverse()
            return path
        for row_change, col_change in directions:
            new_row = row + row_change
            new_col = col + col_change

            if (
                  0 <= new_row < len(grid) 
                  and 0 <= new_col < len(grid[0])
                  ):
                if grid[new_row][new_col] != 1:
                    neighbour = (new_row, new_col)
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                        parent[neighbour] = current
                    
    return None