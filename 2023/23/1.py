from collections import deque
import sys

sys.setrecursionlimit(1000000)

import numpy as np


def dfs(grid, curr_vertex, visited, finish, curr_path, all_paths):
    if curr_vertex == finish:
        all_paths.append(curr_path.copy())
        return 

    visited.add(curr_vertex)

    x, y = curr_vertex
    if grid[x, y] == "." or grid[x, y] == ">":
        if (x, y + 1) not in visited:
            curr_path.append((x, y + 1))
            dfs(grid, (x, y + 1), visited, finish, curr_path, all_paths)
            curr_path.pop()
    if grid[x, y] == "." or grid[x, y] == "<":
        if (x, y - 1) not in visited:
            curr_path.append((x, y - 1))
            dfs(grid, (x, y - 1), visited, finish, curr_path, all_paths)
            curr_path.pop()
    if grid[x, y] == "." or grid[x, y] == "^":
        if (x - 1, y) not in visited:
            curr_path.append((x - 1, y))
            dfs(grid, (x - 1, y), visited, finish, curr_path, all_paths)
            curr_path.pop()
    if grid[x, y] == "." or grid[x, y] == "v":
        if (x + 1, y) not in visited:
            curr_path.append((x + 1, y))
            dfs(grid, (x + 1, y), visited, finish, curr_path, all_paths)
            curr_path.pop()
    visited.remove(curr_vertex)

    return all_paths


if __name__ == "__main__":
    with open("23/input.txt", "r") as f:
        lines = f.readlines()
        grid = np.array([list(line.strip()) for line in lines])
        start = (0, np.where(grid[0] == ".")[0][0])
        finish = (len(grid) - 1, np.where(grid[-1] == ".")[0][0])
        print(start, finish)

    paths = dfs(grid, start, set(), finish, [], [])
    print(max([len(path) for path in paths]))
