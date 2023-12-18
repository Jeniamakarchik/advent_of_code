import numpy as np

def calculate_area(coordinates):
    """ 
    https://en.wikipedia.org/wiki/Shoelace_formula
    """
    area = np.abs(np.sum(coordinates[:-1, 0] * coordinates[1:, 1]) - np.sum(coordinates[1:, 0] * coordinates[:-1, 1])) / 2

    return area

# https://en.wikipedia.org/wiki/Pick's_theorem
# 
# The formula in Wikipedia has A on the left side, but we are looking not for A but for i + b. To achieve that:
# A = i + b/2 - 1 - We subtract i from both sides.
# -i + A = b/2 - 1 - We subtract A from both sides.
# -i = -A + b/2 - 1 - We have a formula for -i, therefore we multiply both sides by -1. This is the step in which "- 1" changes into "+ 1".
# i = A - b/2 + 1 - Now we have a formula for i, but we were looking for i + b, so we add b to both sides. Here "- b/2" changes into "+ b/2".
# i + b = A + b/2 + 1

direction_mapping = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}

if __name__ == "__main__":
    with open("18/input.txt", "r") as f:
        lines = f.readlines()
    
    coordinates = [(0, 0)]


    ind, jnd = 0, 0
    border = 0
    for line in lines:
        _, _, color = line.split()

        direction = direction_mapping[color[-2]]
        meters = int(color[2:-2], 16)

        if direction == 'U':
            ind -= int(meters)
        elif direction == 'D':
            ind += int(meters)
        elif direction == 'R':
            jnd += int(meters)
        elif direction == 'L':
            jnd -= int(meters)
        border += int(meters)
        coordinates.append((ind, jnd))

    coordinates = np.array(coordinates)
    inner_area = calculate_area(coordinates)

    print("Total area:", int(inner_area + border/2 + 1))
