import numpy as np


def get_distance(x1, y1, x2, y2, empty_rows, empty_cols, times=1000000):
    empty_count = 0 
    for i in range(min(x1, x2), max(x1, x2)):
        if i in empty_rows:
            empty_count += 1

    for i in range(min(y1, y2), max(y1, y2)):
        if i in empty_cols:
            empty_count += 1

    return abs(x1 - x2) + abs(y1 - y2) + empty_count * (times - 1) # we have already calculated empty rows and cols in manh distance


if __name__ == "__main__":
    with open("11/input.txt", "r") as f:
        lines = f.readlines()

        empty_rows, empty_cols = set(), set()

        # empty row or column expand 1000000 times
        grid = []
        for ind, line in enumerate(lines):
            num_line = [1 if el == '#' else 0 for el in list(line.strip())]
            grid.append(num_line)
            if np.all(np.array(num_line) == 0):
                empty_rows.add(ind)
        grid = np.array(grid)

        for ind, col in enumerate(grid.T):
            if np.all(col == 0):
                empty_cols.add(ind)
    
    galaxy_coords = np.where(grid == 1)
    galaxy_coords = list(zip(galaxy_coords[0], galaxy_coords[1]))

    total_distance = 0
    for x_coord in galaxy_coords:
        for y_coord in galaxy_coords:
            total_distance += get_distance(x_coord[0], x_coord[1], y_coord[0], y_coord[1], empty_rows, empty_cols)

    print(total_distance // 2)
    