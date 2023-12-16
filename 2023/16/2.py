from collections import deque

import numpy as np

movement = {
    'D': (1, 0),
    'U': (-1, 0),
    'R': (0, 1),
    'L': (0, -1),
}


def check_coord(grid, coord):
    if coord[0] < 0 or coord[0] >= grid.shape[0] or coord[1] < 0 or coord[1] >= grid.shape[1]:
        return False
    return True


def beam_trace(grid, curr_cell=(0, 0), direction='R'):
    visited = set()
    seen = set()

    new_grid = grid.copy()

    path = deque([(curr_cell, direction)])
    while path:
        curr_cell, direction = path.popleft()

        if not check_coord(grid, curr_cell):
            continue

        if (curr_cell, direction) in visited:
            continue

        visited.add((curr_cell, direction))
        seen.add(curr_cell)

        if (grid[curr_cell], direction) in (('/', 'R'), ('\\', 'L')):
            next_cell = (
                curr_cell[0] + movement['U'][0], 
                curr_cell[1] + movement['U'][1]
            )
            path.appendleft((next_cell, 'U'))
        elif (grid[curr_cell], direction) in (('/', 'L'), ('\\', 'R')):
            next_cell = (
                curr_cell[0] + movement['D'][0], 
                curr_cell[1] + movement['D'][1]
            )
            path.appendleft((next_cell, 'D'))
        elif (grid[curr_cell], direction) in (('/', 'U'), ('\\', 'D')):
            next_cell = (
                curr_cell[0] + movement['R'][0], 
                curr_cell[1] + movement['R'][1]
            )
            path.appendleft((next_cell, 'R'))
        elif (grid[curr_cell], direction) in (('/', 'D'), ('\\', 'U')):
            next_cell = (
                curr_cell[0] + movement['L'][0], 
                curr_cell[1] + movement['L'][1]
            )
            path.appendleft((next_cell, 'L'))
        elif grid[curr_cell] == '-' and direction in ('U', 'D'):
            next_cell = (
                curr_cell[0] + movement['L'][0], 
                curr_cell[1] + movement['L'][1]
            )
            path.appendleft((next_cell, 'L'))

            next_cell = (
                curr_cell[0] + movement['R'][0], 
                curr_cell[1] + movement['R'][1]
            )
            path.appendleft((next_cell, 'R'))
        elif grid[curr_cell] == '|' and direction in ('L', 'R'):
            next_cell = (
                curr_cell[0] + movement['U'][0], 
                curr_cell[1] + movement['U'][1]
            )
            path.appendleft((next_cell, 'U'))

            next_cell = (
                curr_cell[0] + movement['D'][0], 
                curr_cell[1] + movement['D'][1]
            )
            path.appendleft((next_cell, 'D'))
        else:
            next_cell = (
                curr_cell[0] + movement[direction][0], 
                curr_cell[1] + movement[direction][1]
            )
            path.appendleft((next_cell, direction))

    return seen
    

if __name__ == "__main__":
    with open("16/input.txt", "r") as f:
        lines = f.readlines()
        grid = np.array([list(line.strip()) for line in lines])

    results = []

    for i in range(grid.shape[0]):
        seen = beam_trace(grid, curr_cell=(i, 0), direction='R')
        results.append(len(seen))
        seen = beam_trace(grid, curr_cell=(i, grid.shape[1] - 1), direction='L')
        results.append(len(seen))
    for j in range(grid.shape[1]):
        seen = beam_trace(grid, curr_cell=(0, j), direction='D')
        results.append(len(seen))
        seen = beam_trace(grid, curr_cell=(grid.shape[0] - 1, j), direction='U')
        results.append(len(seen))

    print(max(results))

