import numpy as np


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    with open("11/input.txt", "r") as f:
        lines = f.readlines()

        # empty row or column expand twice
        grid = []
        for line in lines:
            num_line = [1 if el == '#' else 0 for el in list(line.strip())]
            grid.append(num_line)
            if np.all(np.array(num_line) == 0):
                grid.append(num_line)
        grid = np.array(grid)

        col_idx = 0
        while col_idx < grid.shape[1]:
            if np.all(grid[:, col_idx] == 0):
                grid = np.insert(grid, col_idx + 1, 0, axis=1)
                col_idx += 1
            col_idx += 1
    
    galaxy_coords = np.where(grid == 1)
    galaxy_coords = list(zip(galaxy_coords[0], galaxy_coords[1]))

    total_distance = 0
    for x_coord in galaxy_coords:
        for y_coord in galaxy_coords:
            total_distance += manhattan_distance(x_coord[0], x_coord[1], y_coord[0], y_coord[1])

    print(total_distance // 2)
    