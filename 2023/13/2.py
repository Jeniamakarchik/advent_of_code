import numpy as np


def get_horizontal_mirror(grid):
    middle = len(grid) // 2
    for i in range(1, middle + 1):
        if np.sum(np.abs(grid[:i] - grid[2*i-1:i-1:-1])) == 1:
            return i
        elif np.sum(np.abs(grid[-i:] - grid[-i-1:-2*i-1:-1])) == 1:
            return len(grid) - i
    return 0   


def get_vertical_mirror(grid):
    middle = len(grid[0]) // 2
    for i in range(1, middle + 1):
        if np.sum(np.abs(grid[:, :i] - grid[:, 2*i-1:i-1:-1])) == 1:
            return i
        elif np.sum(np.abs(grid[:, -i:] - grid[:, -i-1:-2*i-1:-1])) == 1:
            return len(grid[0]) - i

    return 0


if __name__ == "__main__":
    with open("13/input.txt", "r") as f:
        lines = f.read().strip().split("\n\n")

    total_mirrors = 0
    for line in lines:
        grid = []
        for row in line.split("\n"):
            grid.append([1 if el == "#" else 0 for el in row])
        grid = np.array(grid)
        
        row_ind = get_horizontal_mirror(grid)
        col_ind = get_vertical_mirror(grid)
        
        total_mirrors += col_ind
        total_mirrors += 100 * row_ind

    print(total_mirrors)
