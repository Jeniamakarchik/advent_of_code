from collections import defaultdict
from itertools import combinations

import numpy as np


# def process_two_antenas(antena_a, antena_b, grid):
#     x1, y1 = antena_a
#     x2, y2 = antena_b

#     a = (y2 - y1) / (x2 - x1)
#     b = y1 - a * x1

#     deltax = np.abs(x2 - x1)

#     new_coordinates = []
#     x_new, y_new = np.max((x1, x2)), int(a * np.max((x1, x2)) + b)
#     while check_coordinates(x_new, y_new, grid.shape):
#         new_coordinates.append((x_new, y_new))
#         x_new += deltax
#         y_new = int(a * x_new + b)

#     x_new, y_new = np.min((x1, x2)), int(a * np.min((x1, x2)) + b)
#     while check_coordinates(x_new, y_new, grid.shape):
#         new_coordinates.append((x_new, y_new))
#         x_new -= deltax
#         y_new = int(a * x_new + b)

#     return new_coordinates


def process_two_antenas(antena_a, antena_b, grid):
    x1, y1 = antena_a
    x2, y2 = antena_b

    deltax = x2 - x1
    deltay = y2 - y1

    new_coordinates = []
    for direction in (1, -1):
        while True:
            x1_new = x1 + direction * deltax
            y1_new = y1 + direction * deltay
            if not check_coordinates(x1_new, y1_new, grid.shape):
                break
            new_coordinates.append((x1_new, y1_new))
            x1 = x1_new
            y1 = y1_new

        while True:
            x2_new = x2 + direction * deltax
            y2_new = y2 + direction * deltay
            if not check_coordinates(x2_new, y2_new, grid.shape):
                break
            new_coordinates.append((x2_new, y2_new))
            x2 = x2_new
            y2 = y2_new

    return new_coordinates


def check_coordinates(x, y, shape):
    return 0 <= x < shape[0] and 0 <= y < shape[1]


if __name__ == "__main__":
    with open("08/input.txt", "r") as f:
        grid = np.array([list(line.strip()) for line in f])

    antena_coordinates = defaultdict(list)
    antinodes = set()

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == ".":
                continue
            antena_coordinates[grid[i, j]].append((i, j))

    for coordinates in antena_coordinates.values():
        for a, b in combinations(coordinates, 2):
            new_coordinates = process_two_antenas(a, b, grid)
            antinodes.update(new_coordinates)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] in antena_coordinates:
                print(grid[i, j], end="")
            elif (i, j) in antinodes:
                print("#", end="")
            else:
                print(".", end="")
        print()

    print(len(antinodes))
