from collections import deque

import numpy as np

def check_coord(shape, coord):
    return coord[0] >= 0 and coord[0] < shape[0] and coord[1] >= 0 and coord[1] < shape[1]


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
STEPS = 64


# https://medium.com/towards-data-science/graph-theory-bfs-shortest-path-problem-on-a-grid-1437d5cb4023
# keeping track of parity as we need even number of steps to return to the same cell


if __name__ == "__main__":
    with open("21/input.txt", "r") as f:
        lines = f.readlines()
        grid = np.array([list(line.strip()) for line in lines])
        start = np.where(grid == "S")
        start = (start[0][0], start[1][0])
        print(start) 

        grid = np.where(grid == "#", False, True)
        parity = np.zeros_like(grid, dtype=np.int8)

    coord_queue = deque([start])
    num_step_queue = deque([0])
    visited = set()
    while coord_queue and num_step_queue[0] <= STEPS:
        pos = coord_queue.popleft()
        step = num_step_queue.popleft()

        if pos in visited:
            continue

        if step % 2 == 0:
            parity[pos] = 1
        else:
            parity[pos] = -1

        for d in directions:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if check_coord(grid.shape, new_pos) and grid[new_pos]:
                coord_queue.append(new_pos)
                num_step_queue.append(step + 1)
        
        visited.add(pos)

    visualisation = np.where(~grid, "#", np.where(parity == 1 if STEPS % 2 == 0 else -1, '0', '.'))
    print(visualisation)
    print(np.sum(parity == 1 if STEPS % 2 == 0 else -1))
