
import time
import numpy as np

def move_up(x, y):
    return x - 1, y

def move_down(x, y):
    return x + 1, y

def move_left(x, y):
    return x, y - 1

def move_right(x, y):
    return x, y + 1

turn = {
    0: move_up,
    1: move_right,
    2: move_down,
    3: move_left
}


def loop_checker(free_spots, obsticles, new_obsticle, start_pos):
    next_x, next_y = start_pos

    visited = set()
    curr_turn, curr_pos = 0, start_pos
    while True:
        x, y = curr_pos
        if (curr_pos, curr_turn) in visited:
            # print("X", end="")
            return True

        visited.add((curr_pos, curr_turn))
        next_x, next_y = turn[curr_turn](x, y)
        
        if (next_x, next_y) in obsticles or (next_x, next_y) == new_obsticle:
            curr_turn = (curr_turn + 1) % 4
        elif (next_x, next_y) in free_spots:
            # print("0", end="")
            curr_pos = (next_x, next_y)
        else:
            return False     
            


if __name__ == "__main__":
    with open("06/input.txt", "r") as f:
        # create numpy array
        grid = [line.strip() for line in f.readlines()]
        grid = np.array([list(row) for row in grid])
        shape = grid.shape

    # find coordinates of ^
    start_x, start_y = np.where(grid == "^")
    x, y = start_x[0], start_y[0]

    free_spots = np.where(grid == ".")
    free_spots = set(zip(free_spots[0], free_spots[1]))
    free_spots.add((x, y))

    obsticles = np.where(grid == "#")
    obsticles = set(zip(obsticles[0], obsticles[1]))

    loops_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in free_spots:
                if loop_checker(free_spots, obsticles, (i, j), (x, y)):
                    loops_count += 1
    
    print()
    print(loops_count)
