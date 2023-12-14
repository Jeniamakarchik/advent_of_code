import numpy as np


def tilt_north(grid):
    for col_ind in range(len(grid[0])):
        col = grid[:, col_ind]
        rocks = np.where(col == 'O')[0]
        borders = np.where(col == '#')[0]
        borders = np.concatenate(([-1], borders, [len(col)]))

        ind = 1
        while ind < len(borders):
            l_border, r_border = borders[ind - 1] + 1, borders[ind]
            rocks_between = np.sum((rocks >= l_border) & (rocks < r_border))

            col[l_border:l_border + rocks_between] = ['O']
            col[l_border + rocks_between:r_border] = ['.']
            ind += 1

    return grid


def calculate_load(grid):
    rocks = np.where(grid == 'O')
    return np.sum(len(grid) - rocks[0])


# def tilt_north_and_count_load(grid):
#     total_load = 0
#     for row in grid:
#         rocks = np.where(row == 'O')[0]
#         borders = np.where(row == '#')[0]

#         if len(rocks):
#             ind = 1
#             while ind < len(borders):
#                 l_border, r_border = borders[ind - 1], borders[ind]
#                 rocks_between = (rocks > l_border) & (rocks < r_border)

#                 row_load = sum([len(row) - l_border - i for i in range(np.sum(rocks_between))])
#                 total_load += row_load
#                 ind += 1

#     return total_load


if __name__ == "__main__":
    with open("14/input.txt", "r") as f:
        lines = f.readlines()
        grid = np.array([list(line.strip()) for line in lines])
    
    print("Total load:", calculate_load(tilt_north(grid)))

    # total_load = tilt_north_and_count_load(grid)
    # print("Total load:", total_load)
