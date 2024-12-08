from collections import defaultdict
from itertools import combinations

import matplotlib.pyplot as plt
import numpy as np


# def process_two_antenas(antena_a, antena_b):
#     x1, y1 = antena_a
#     x2, y2 = antena_b

#     deltax = x2 - x1
#     deltay = y2 - y1

#     new_coordinates = []
#     for direction in (1, -1):
#         x1_new = x1 + direction * deltax
#         y1_new = y1 + direction * deltay
#         x2_new = x2 + direction * deltax
#         y2_new = y2 + direction * deltay

#         new_coordinates.append((x1_new, y1_new))
#         new_coordinates.append((x2_new, y2_new))

#     new_coordinates = set(new_coordinates) - set((antena_a, antena_b))

#     return new_coordinates.pop() + new_coordinates.pop()

def process_two_antenas(antena_a, antena_b):
    x1, y1 = antena_a
    x2, y2 = antena_b

    a = np.round((y2 - y1) / (x2 - x1),0)
    b = y1 - a * x1

    deltax = np.abs(x2 - x1)

    x1_new = np.max((x1, x2)) + deltax
    y1_new = a * x1_new + b

    x2_new = np.min((x1, x2)) - deltax
    y2_new = a * x2_new + b

    return x1_new, y1_new, x2_new, y2_new


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
            plt.plot(i, j, "r*")

    for coordinates in antena_coordinates.values():
        for a, b in combinations(coordinates, 2):
            x1, y1, x2, y2 = process_two_antenas(a, b)
            if check_coordinates(x1, y1, grid.shape):
                antinodes.add((x1, y1))
            if check_coordinates(x2, y2, grid.shape):
                antinodes.add((x2, y2))

    plt.xlim(0, grid.shape[0])
    plt.ylim(0, grid.shape[1])
    plt.grid()
    plt.show()
    print(len(antinodes))
