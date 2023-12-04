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


def process_pile(pile, count=0):
    pile_top_score = is_winning(pile[0])
    if len(pile) == 1 or pile_top_score == 0:
        return 1

    local_count = 1
    for i in range(1, pile_top_score + 1):
        local_count += process_pile(pile[i:])
    
    return local_count


if __name__ == "__main__":
    with (open("04/input.txt", "r")) as f:
        pile = f.readlines()

    total_number = 0
    for i in range(len(pile)):
        total_number += process_pile(pile[i:])

    print("Total winning points:", total_number)
