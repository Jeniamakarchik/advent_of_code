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
        print(curr_cell, direction)

        if not check_coord(grid, curr_cell):
            continue

        if (curr_cell, direction) in visited:
            continue
        
        new_grid[curr_cell] = '#'

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

    print(new_grid)

    return seen
    

if __name__ == "__main__":
    with open("16/input.txt", "r") as f:
        lines = f.readlines()
        grid = np.array([list(line.strip()) for line in lines])
        
    print(grid)
    seen = beam_trace(grid)
    print(len(seen))
