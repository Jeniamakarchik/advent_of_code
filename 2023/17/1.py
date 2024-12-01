import numpy as np

CONSECUTIVE_BLOCKS = 3


# NOTE: Djikstra's Algorithm

if __name__ == "__main__":
    with open("17/input.txt", "r") as f:
        lines = f.readlines()
        grid = np.array([list(line.strip()) for line in lines])
    
    start = (0, 0)
    finish = (len(grid[0]) - 1, len(grid) - 1)
    print(grid)
