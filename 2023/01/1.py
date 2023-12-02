import re

if __name__ == "__main__":
    with open("01/input.txt", "r") as f:
        calibration_sum = 0
        for line in f.readlines():
            digits = re.findall(r"\d", line)
            first = digits[0]
            last = digits[-1]

            number = int(first + last)
            calibration_sum += number

        print(calibration_sum)
