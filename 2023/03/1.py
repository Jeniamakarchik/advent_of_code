def is_valid_pos(pos, grid):
    x,y = pos
    if x < 0 or y < 0:
        return False
    try:
        grid[x][y]
        return True
    except IndexError:
        return False


def is_symbol(symbol):
    return symbol != "." and symbol != "\n" and not symbol.isdigit()


def check_symbol(grid, coord):
    x, y = coord
    offsets = [(-1, -1), (-1, 0), (-1, 1), 
              (0, -1),          (0, 1),
              (1, -1), (1, 0), (1, 1)]

    for offset in offsets:
        if is_valid_pos((x + offset[0], y + offset[1]), grid):
            x_, y_ = x + offset[0], y + offset[1]
            if is_symbol(grid[x_][y_]):
                print(f"({x_}, {y_}) {grid[x_][y_]}", end = " ")
                return True
    
    return False
    

if __name__ == "__main__":
    with open("03/input.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    buffer = list()
    coords = list()
    numbers = list()

    for ind, line in enumerate(grid):
        for jnd, el in enumerate(line):
            if el.isdigit():
                buffer.append(el)
                coords.append((ind, jnd))
            else:
                if buffer:
                    number = int("".join(buffer))
                    for coord in coords:
                        if check_symbol(grid, coord):
                            numbers.append(number)
                            print(number)
                            break

                    buffer.clear()
                    coords.clear()

        if buffer:
                    number = int("".join(buffer))
                    for coord in coords:
                        if check_symbol(grid, coord):
                            numbers.append(number)
                            print(number)
                            break

                    buffer.clear()
                    coords.clear()
        
    
    with open('output1.txt', 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

    print(sum(numbers))
