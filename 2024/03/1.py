import re


if __name__ == "__main__":
    with open("03/input.txt", "r") as f:
        program = f.read()

    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = pattern.findall(program)

    result = 0
    for i in range(len(matches)):
        result += int(matches[i][0]) * int(matches[i][1])
    print(result)
