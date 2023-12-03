from collections import defaultdict

GEAR_SYMBOL = "*"

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

    for offset in offsets:
        if is_valid_pos((x + offset[0], y + offset[1]), grid):
            x_, y_ = x + offset[0], y + offset[1]
            if grid[x_][y_] == GEAR_SYMBOL:
                return (True, (x_, y_))
    
    return (False, (-1, -1))


if __name__ == "__main__":
    with open("03/input.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    buffer = list()
    coords = list()
    numbers = list()

    gear_coord_to_number = defaultdict(list)

    for ind, line in enumerate(grid):
        for jnd, el in enumerate(line):
            if el.isdigit():
                buffer.append(el)
                coords.append((ind, jnd))
            else:
                if buffer:
                    number = int("".join(buffer))
                    for coord in coords:
                        is_symbol, gear_coord = check_symbol(grid, coord)
                        if is_symbol:
                            gear_coord_to_number[gear_coord].append(number)
                            break

                    buffer.clear()
                    coords.clear()

        if buffer:
            number = int("".join(buffer))
            for coord in coords:
                is_symbol, gear_coord = check_symbol(grid, coord)
                if is_symbol:
                    gear_coord_to_number[gear_coord].append(number)
                    break

            buffer.clear()
            coords.clear()
        
    total_gear_ratio = 0
    with open('output1.txt', 'w') as file:
        for coord, numbers in gear_coord_to_number.items():
            if len(numbers) == 2:
                gear_ratio = int(numbers[0]) * int(numbers[1])
                total_gear_ratio += gear_ratio

    print(total_gear_ratio)
