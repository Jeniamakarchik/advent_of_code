import numpy as np


if __name__ == "__main__":
    with open("01/input.txt", "r") as f:
        right_array, left_array = [], []
        for line in f:
            right, left = line.split()
            right_array.append(int(right))
            left_array.append(int(left))

    right_array.sort()
    left_array.sort()

    print(np.sum(np.abs(np.array(right_array) - np.array(left_array))))
