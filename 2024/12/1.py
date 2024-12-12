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

def check_cell(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return False
    return True


def get_sector_value(grid, start_x, start_y):
    visited = set()
    stack = [(start_x, start_y)]

    curr_label = grid[start_x][start_y]
    perimeter, square = 0, 0

    while stack:
        x, y = stack.pop()
        if grid[x][y] != curr_label or (x, y) in visited:
            continue
        
        square += 1
        for move in MOVES:
            move_x, move_y = move(grid, x, y)
            if not check_cell(grid, move_x, move_y) or grid[move_x][move_y] != curr_label:
                perimeter += 1
                continue

            if (move_x, move_y) not in visited:
                stack.append((move_x, move_y))
        
        visited.add((x, y))

    return perimeter, square, visited


if __name__ == "__main__":
    with open("12/input.txt", "r") as f:
        grid = [[c for c in line.strip()] for line in f.readlines()]

    sum_values = 0
    visited = set()
    for start_x, start_y in [(x, y) for x in range(len(grid)) for y in range(len(grid[0]))]:
        if (start_x, start_y) in visited:
            continue

        perimeter, square, visited_zone = get_sector_value(grid, start_x, start_y)
        sum_values += perimeter * square
        visited.update(visited_zone)
        print(f"Start: {start_x}, {start_y}, perimeter: {perimeter}, square: {square}")

    print(sum_values)
