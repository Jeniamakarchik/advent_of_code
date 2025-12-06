import numpy as np


if __name__ == "__main__":
    with open("03/input.txt", "r") as f:
        joltage = 0
        for line in f:
            bank = np.array([int(x) for x in line.strip()])
            max_idx_l = bank[:-1].argmax()
            max_idx_r = bank[max_idx_l + 1 :].argmax() + max_idx_l + 1
            joltage += bank[max_idx_l]*10 + bank[max_idx_r]

    print(joltage)
