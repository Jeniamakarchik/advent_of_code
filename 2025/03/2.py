import numpy as np


if __name__ == "__main__":
    with open("03/input.txt", "r") as f:
        joltage = 0
        for line in f:
            bank = np.array([int(x) for x in line.strip()])
            battery = 0
            max_idx_l = 0
            i = 12
            while i > 0:
                i -= 1
                print(bank[max_idx_l:-i] if i != 0 else bank[max_idx_l:])
                max_idx_r = bank[max_idx_l:-i].argmax() if i != 0 else bank[max_idx_l:].argmax()
                battery = battery*10 + bank[max_idx_l + max_idx_r]
                max_idx_l += max_idx_r + 1
            joltage += battery
            print(battery)

    print(joltage)
