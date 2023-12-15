from collections import OrderedDict

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

    boxes = dict()
    for line in sequence:
        if '-' in line:
            label = line[:-1]
            hash_value = get_hash(label)
            if hash_value in boxes and label in boxes[hash_value]:
                del boxes[hash_value][label]

        elif '=' in line:
            label, number = line.split('=')
            hash_value = get_hash(label)
            if hash_value not in boxes:
                boxes[hash_value] = OrderedDict()

            boxes[hash_value][label] = int(number)

    
    total_focal_sum = 0
    for box, lenses in boxes.items():
        print("Box", box)
        box_focal_strength = 0
        for ind, (label, strength) in enumerate(lenses.items()):
            box_focal_strength += (ind + 1) * strength
            print("  ", label, strength, "pos:", (ind + 1), "strength:", strength)
        total_focal_sum += box_focal_strength * (1 + box)

    print("Total focal sum:", total_focal_sum)
