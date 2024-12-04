def check_letter(i, j, word_grid):
    if i < 0 or i >= len(word_grid) or j < 0 or j >= len(word_grid[i]):
        return

    xmas_count = 0
    coordinates = []
    if i > 2:
        if word_grid[i-1][j] == "M" and word_grid[i-2][j] == "A" and word_grid[i-3][j] == "S":
            print("\t", "up")
            coordinates.extend([(i-1, j), (i-2, j), (i-3, j)])
            xmas_count += 1
        if j > 2:
            if word_grid[i-1][j-1] == "M" and word_grid[i-2][j-2] == "A" and word_grid[i-3][j-3] == "S":
                print("\t", "up-left")
                xmas_count += 1
                coordinates.extend([(i-1, j-1), (i-2, j-2), (i-3, j-3)])
        if j + 3 < len(word_grid[i]):
            if word_grid[i-1][j+1] == "M" and word_grid[i-2][j+2] == "A" and word_grid[i-3][j+3] == "S":
                print("\t", "up-right")
                xmas_count += 1
                coordinates.extend([(i-1, j+1), (i-2, j+2), (i-3, j+3)])
    if i + 3 < len(word_grid):
        if word_grid[i+1][j] == "M" and word_grid[i+2][j] == "A" and word_grid[i+3][j] == "S":
            print("\t", "down")
            xmas_count += 1
            coordinates.extend([(i+1, j), (i+2, j), (i+3, j)])
        if j > 2:
            if word_grid[i+1][j-1] == "M" and word_grid[i+2][j-2] == "A" and word_grid[i+3][j-3] == "S":
                print("\t", "down-left")
                xmas_count += 1
                coordinates.extend([(i+1, j-1), (i+2, j-2), (i+3, j-3)])
        if j + 3 < len(word_grid[i]):
            if word_grid[i+1][j+1] == "M" and word_grid[i+2][j+2] == "A" and word_grid[i+3][j+3] == "S":
                print("\t", "down-right")
                xmas_count += 1
                coordinates.extend([(i+1, j+1), (i+2, j+2), (i+3, j+3)])
    if j > 2:
        if word_grid[i][j-1] == "M" and word_grid[i][j-2] == "A" and word_grid[i][j-3] == "S":
            print("\t", "left")
            xmas_count += 1
            coordinates.extend([(i, j-1), (i, j-2), (i, j-3)])
    if j + 3 < len(word_grid[i]):
        if word_grid[i][j+1] == "M" and word_grid[i][j+2] == "A" and word_grid[i][j+3] == "S":
            print("\t", "right")
            xmas_count += 1
            coordinates.extend([(i, j+1), (i, j+2), (i, j+3)])
    
    return xmas_count, coordinates


if __name__ == "__main__":
    with open("04/input.txt", "r") as f:
        word_grid = []
        for line in f:
            word_grid.append(line.strip())
    
    xmas_count = 0
    coordinates = []
    for i in range(len(word_grid)):
        for j in range(len(word_grid[i])):
            if word_grid[i][j] != "X":
                continue
            
            print(i, j)
            xmas_count_letter, coordinates_letter = check_letter(i, j, word_grid)
            xmas_count += xmas_count_letter
            if coordinates_letter:
                coordinates.append((i, j))
                coordinates.extend(coordinates_letter)

    for i in range(len(word_grid)):
        for j in range(len(word_grid[i])):
            if (i, j) in coordinates:
                print(word_grid[i][j], end="")
            else:
                print(".", end="")
        print()

    print(xmas_count)
