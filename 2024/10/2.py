import numpy as np


def move_up(grid, x, y):
    return x - 1, y


def move_down(grid, x, y):
    return x + 1, y


def move_left(grid, x, y):
    return x, y - 1


def move_right(grid, x, y):
    return x, y + 1


MOVES = [move_up, move_down, move_left, move_right]


def get_trail_value(grid, start_x, start_y):
    distinct_ways = 0
    stack = [(start_x, start_y, set(), move) for move in MOVES]

    while len(stack) > 0:
        x, y, visited, move = stack.pop(0)
        new_x, new_y = move(grid, x, y)
        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
            continue

        if (new_x, new_y) not in visited and grid[new_x][new_y] == grid[x][y] + 1:
            if grid[new_x][new_y] == 9:
                distinct_ways += 1
            else:
                # add new tuple (x,y) to visited set
                visited = visited.copy()
                visited.add((x, y))
                for new_move in MOVES:
                    stack.insert(0, (new_x, new_y, visited, new_move))
        
    return distinct_ways


if __name__ == "__main__":
    with open("10/input.txt", "r") as f:
        grid = [[int(c) for c in line.strip()] for line in f.readlines()]

    start_points = np.argwhere(np.array(grid) == 0)

    sum_values = 0
    for start_x, start_y in start_points:
        value = get_trail_value(grid, start_x, start_y)
        sum_values += value
        print(f"Start: {start_x}, {start_y}, Value: {value}")

    print(sum_values)
