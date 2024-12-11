from collections import Counter
from pprint import pprint


if __name__ == "__main__":
    with open("11/input.txt", "r") as f:
        numbers = [int(x) for x in f.read().split(" ")]

    amount = Counter(numbers)
                   
    for i in range(75):
        # pprint(amount)
        upd_amount = Counter()
        for number, value in amount.items():
            if number == 0:
                upd_amount.update({1: value})
            elif len(str(number)) %2 == 0:
                length = len(str(number)) // 2
                part_1 = int(str(number)[:length])
                part_2 = int(str(number)[length:])

                upd_amount.update({part_1: value})
                upd_amount.update({part_2: value})
            else:
                upd_amount.update({number*2024: value})
            
            amount = upd_amount

    print(sum(amount.values()))
