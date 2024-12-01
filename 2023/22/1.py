import re

if __name__ == "__main__":
    with open("22/input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            x1, y1, z1, x2, y2, z2 = map(int, re.findall(r"(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)", line)[0])
            
