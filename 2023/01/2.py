import re
from unicodedata import name


digits = {
        k: v for v in "123456789" for k in [v, name(v).removeprefix("DIGIT ").lower()]
    }


if __name__ == "__main__":
    with open("01/input.txt", "r") as f: 
        pattern = r"(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))"
        print(pattern)

        calibration_sum = 0
        for line in f.readlines():
            found = re.findall(pattern, 2*line)
            first = digits[found[0]]
            last = digits[found[-1]]

            number = int(first + last)
            calibration_sum += number
        print(calibration_sum)
