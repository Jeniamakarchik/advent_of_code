import numpy as np


directions = {
    '|': [(-1, 0), (1, 0)], # is a vertical pipe connecting north and south.
    '-': [(0, -1), (0, 1)], # is a horizontal pipe connecting east and west.
    'L': [(-1, 0), (0, 1)], # is a 90-degree bend connecting north and east.
    'J': [(-1, 0), (0, -1)], # is a 90-degree bend connecting north and west.
    '7': [(1, 0), (0, -1)], # is a 90-degree bend connecting south and west.
    'F': [(1, 0), (0, 1)], # is a 90-degree bend connecting south and east.
    '.': [(0, 0), (0, 0)], # is ground; there is no pipe in this tile.
}

moves_to_coord = {
    'south': (1, 0),
    'north': (-1, 0),
    'east': (0, 1),
    'west': (0, -1),
}

from_to = {
    'south': 'north',
    'north': 'south',
    'east': 'west',
    'west': 'east',
}

def get_direction(pos, grid):
    directions = []
    moves = []

    if pos[0] > 0 and grid[pos[0] - 1][pos[1]] in ['7', 'F', '|']:
        # check north
        print(grid[pos[0] - 1, pos[1]])
        directions.append((-1, 0))
        moves.append("south")
    if pos[0] < len(grid) - 1 and grid[pos[0] + 1][pos[1]] in ['L', 'J', '|']:
        # check south
        print(grid[pos[0] + 1, pos[1]])
        directions.append((1, 0))
        moves.append("north")
    if pos[1] > 0 and grid[pos[0]][pos[1] - 1] in ['-', 'L', 'F']:
        # check west
        print(grid[pos[0], pos[1] - 1])
        directions.append((0, -1))
        moves.append("east")
    if pos[1] < len(grid[0]) - 1 and grid[pos[0]][pos[1] + 1] in ['-', '7', 'J']:
        # check east
        print(grid[pos[0], pos[1] + 1])
        directions.append((0, 1))
        moves.append("west")
    
    return directions, moves


def make_move(pos, grid, come_from=None):
    if come_from == "north":
        if grid[pos[0]][pos[1]] == '|':
            return "south"
        elif grid[pos[0]][pos[1]] == 'L':
            return "east"
        elif grid[pos[0]][pos[1]] == 'J':
            return "west"
    elif come_from == "south":
        if grid[pos[0]][pos[1]] == '|':
            return "north"
        elif grid[pos[0]][pos[1]] == '7':
            return "west"
        elif grid[pos[0]][pos[1]] == 'F':
            return "east"
    elif come_from == "east":
        if grid[pos[0]][pos[1]] == '-':
            return "west"
        elif grid[pos[0]][pos[1]] == 'L':
            return "north"
        elif grid[pos[0]][pos[1]] == 'F':
            return "south"
    elif come_from == "west":
        if grid[pos[0]][pos[1]] == '-':
            return "east"
        elif grid[pos[0]][pos[1]] == 'J':
            return "north"
        elif grid[pos[0]][pos[1]] == '7':
            return "south"
    else:
        raise Exception("Invalid move")




if __name__ == "__main__":
    with open("10/input.txt", "r") as f:
        lines = f.readlines()

    # Remove newline characters from each line
    grid = np.array([list(line.strip()) for line in lines])

    start_coord = np.where(grid == 'S')
    start_coord = (start_coord[0][0], start_coord[1][0])
    directions, moves = get_direction(start_coord, grid)

    next_coord_a = (start_coord[0] + directions[0][0], start_coord[1] + directions[0][1])
    next_coord_b = (start_coord[0] + directions[1][0], start_coord[1] + directions[1][1])

    come_form_a = moves[0]
    come_form_b = moves[1]

    steps = 1
    while next_coord_a != next_coord_b:
        print(next_coord_a, next_coord_b)

        next_move_a = make_move(next_coord_a, grid, come_form_a)
        next_move_b = make_move(next_coord_b, grid, come_form_b)

        come_form_a = from_to[next_move_a]
        come_form_b = from_to[next_move_b]

        next_coord_a = (next_coord_a[0] + moves_to_coord[next_move_a][0], next_coord_a[1] + moves_to_coord[next_move_a][1])
        next_coord_b = (next_coord_b[0] + moves_to_coord[next_move_b][0], next_coord_b[1] + moves_to_coord[next_move_b][1])

        steps += 1
    print(steps)
