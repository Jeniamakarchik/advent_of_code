def check_letter(i, j, word_grid):
    if i < 1 or i >= len(word_grid) - 1 or j < 1 or j >= len(word_grid[i])-1:
        return False
    
    x_string = "".join([word_grid[i-1][j-1], word_grid[i-1][j+1], word_grid[i+1][j-1], word_grid[i+1][j+1]])
    if x_string == "MMSS" or x_string == "SSMM" or x_string == "MSMS" or x_string == "SMSM":
        return True

    return False


if __name__ == "__main__":
    with open("04/input.txt", "r") as f:
        word_grid = []
        for line in f:
            word_grid.append(line.strip()[::-1])
    
    xmas_count = 0
    coordinates = []
    for i in range(len(word_grid)):
        for j in range(len(word_grid[i])):
            if word_grid[i][j] != "A":
                continue
            
            if check_letter(i, j, word_grid):
                xmas_count += 1
                coordinates.extend([(i, j), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)])

    for i in range(len(word_grid)):
        for j in range(len(word_grid[i])):
            if (i, j) in coordinates:
                print(word_grid[i][j], end="")
            else:
                print(".", end="")
        print()

    print(xmas_count)
