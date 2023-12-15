def get_hash(line):
    value = 0
    for el in line:
        value += ord(el)
        value *= 17
        value %= 256
    return value


if __name__ == "__main__":
    with open("15/input.txt", "r") as f:
        sequence  = f.read().strip().split(",")
    
    print('Total hash:', sum([get_hash(line) for line in sequence]))
