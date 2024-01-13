from collections import deque, defaultdict
import sys

sys.setrecursionlimit(1000000)

import numpy as np

class Graph:
    def __init__(self, grid):
        self.grid_size = grid.shape

        self.vertexes = set()
        self.edges = defaultdict(set)
        self.dist = {}

        self._grah_from_grid(grid)
        print('Initial amount of edges: ', len(self.edges))
        self._contract_edges()
        print('Amount of edges after contraction: ', len(self.edges))

    def add_edge(self, u, v, d):
        self.edges[u].add(v)
        self.edges[v].add(u)

        self.dist[(u, v)] = d
        self.dist[(v, u)] = d

    def get_neighbors(self, u):
        return list(self.edges[u])

    def flatten_idx(self, idx):
        return idx[0] * self.grid_size[0] + idx[1]

    def unflatten_idx(self, idx):
        return (idx // self.grid_size[0], idx % self.grid_size[0])

    def check_idx(self, idx):
        return 0 <= idx[0] < self.grid_size[0] and 0 <= idx[1] < self.grid_size[1]

    def _grah_from_grid(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i, j] != "#":
                    for move in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                        if self.check_idx((i + move[0], j + move[1])) and grid[i + move[0], j + move[1]] != "#":
                            self.add_edge(
                                self.flatten_idx((i, j)), 
                                self.flatten_idx((i + move[0], j + move[1])), 
                                1
                            )

        self.vertexes = set(self.edges.keys())

    def _contract_edges(self):
        for u in self.vertexes:
            if len(self.edges[u]) == 2:
                v1, v2 = list(self.edges[u])
                self.edges[v1].remove(u)
                self.edges[v2].remove(u)
                self.edges[v1].add(v2)
                self.edges[v2].add(v1)
                self.edges.pop(u)

                self.dist[(v1, v2)] = self.dist[(u, v1)] + self.dist[(u, v2)]
                self.dist[(v2, v1)] = self.dist[(u, v1)] + self.dist[(u, v2)]

                del self.dist[(u, v1)]
                del self.dist[(u, v2)]
                del self.dist[(v1, u)]
                del self.dist[(v2, u)]


def dfs(graph, curr_vertex, visited, finish, curr_path, all_paths):
    if curr_vertex == finish:
        all_paths.append(curr_path.copy())
        return

    visited.add(curr_vertex)
    for next_vertex in graph.get_neighbors(curr_vertex):
        if next_vertex not in visited:
            curr_path.append(graph.dist[(curr_vertex, next_vertex)])
            dfs(graph, next_vertex, visited, finish, curr_path, all_paths)
            curr_path.pop()
    visited.remove(curr_vertex)

    return all_paths


# def dfs(grid, curr_vertex, visited, finish, curr_path, all_paths):
#     if curr_vertex == finish:
#         all_paths.append(curr_path.copy())
#         return

#     visited.add(curr_vertex)

#     x, y = curr_vertex
#     if grid[x, y] != "#":
#         for move in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
#             if (x + move[0], y + move[1]) not in visited:
#                 curr_path.append((x + move[0], y + move[1]))
#                 dfs(grid, (x + move[0], y + move[1]), visited, finish, curr_path, all_paths)
#                 curr_path.pop()
#     visited.remove(curr_vertex)

#     return all_paths


if __name__ == "__main__":
    with open("23/input.txt", "r") as f:
        lines = f.readlines()
        grid = np.array([list(line.strip()) for line in lines])
        start = (0, np.where(grid[0] == ".")[0][0])
        finish = (len(grid) - 1, np.where(grid[-1] == ".")[0][0])

        graph = Graph(grid)
        from pprint import pprint

        pprint(graph.edges)

        print(start, finish)

    paths = dfs(graph, graph.flatten_idx(start), set(), graph.flatten_idx(finish), [], [])
    print(max([sum(path) for path in paths]))
