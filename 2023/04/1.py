import re

card_patthern = re.compile(r"^Card +\d+:(( *\d+)+) \|(( *\d+)+)$")

if __name__ == "__main__":
    with (open("04/input.txt", "r")) as f:
        total_winning = 0
        for line in f.readlines():
            match = re.match(card_patthern, line)
            if match:
                winning = set(re.split(' +', match.group(1).strip()))
                actual = set(re.split(' +', match.group(3).strip()))

                winning_number = len(winning.intersection(actual))
                winning_points = 2 ** (winning_number - 1) if winning_number > 0 else 0

                total_winning += winning_points

    print("Total winning points:", total_winning)
