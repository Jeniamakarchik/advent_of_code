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


if __name__ == "__main__":
    with open("06/input.txt", "r") as f:
        # create numpy array
        grid = [line.strip() for line in f.readlines()]
        grid = np.array([list(row) for row in grid])

        shape = grid.shape


    # find coordinates of ^
    start_x, start_y = np.where(grid == "^")
    x, y = start_x[0], start_y[0]

    curr_turn = 0
    while x >= 0 and x < shape[0] and y >= 0 and y < shape[1]:
        next_x, next_y = turn[curr_turn % 4](x, y)
        
        if next_x < 0 or next_x >= shape[0] or next_y < 0 or next_y >= shape[1]:
            break
        elif grid[next_x, next_y] == "#":
            # find next turn
            curr_turn += 1
            next_x, next_y = turn[curr_turn % 4](x, y)

        x, y = next_x, next_y
        grid[x, y] = "X"
        # print("\033c")
        # print(grid)
        # time.sleep(0.1)
    
    print((grid == "X").sum())
