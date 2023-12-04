import re

card_patthern = re.compile(r"^Card +\d+:(( *\d+)+) \|(( *\d+)+)$")

def is_winning(line):
    print(line, end=' ')
    match = re.match(card_patthern, line)
    if match:
        winning = set(re.split(' +', match.group(1).strip()))
        actual = set(re.split(' +', match.group(3).strip()))

        return len(winning.intersection(actual))
    else:
        return 0


def process_pile(points, count=0):
    if len(points) == 1 or points == 0:
        return 1

    local_count = 1
    for i in range(1, points[0] + 1):
        local_count += process_pile(points[i:])
    
    return local_count


if __name__ == "__main__":
    with (open("04/input.txt", "r")) as f:
        pile = f.readlines()

    points = []
    for line in pile:
        points.append(is_winning(line))
    
    total_number = 0
    for i in range(len(pile)):
        total_number += process_pile(points[i:])

    print("Total winning points:", total_number, "Right answer: 9236992")
