def is_valid_pos(pos, grid):
    x,y = pos
    if x < 0 or y < 0:
        return False
    try:
        grid[x][y]
        return True
    except IndexError:
        return False


def check_symbol(grid, coord):
    x, y = coord
    offsets = [(-1, -1), (-1, 0), (-1, 1), 
              (0, -1),          (0, 1),
              (1, -1), (1, 0), (1, 1)]

    rolls_nearby = 0
    for offset in offsets:
        if is_valid_pos((x + offset[0], y + offset[1]), grid):
            x_, y_ = x + offset[0], y + offset[1]
            if grid[x_][y_] == "@":
                rolls_nearby += 1
    
    return rolls_nearby < 4


if __name__ == "__main__":
    with open("2025/04/input.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    total = 0
    positions = []
    for ind, line in enumerate(grid):
        for jnd, el in enumerate(line):
            if el == ".":
                continue

            if check_symbol(grid, (ind, jnd)):
                total += 1
                positions.append((ind, jnd))

    print(total)
