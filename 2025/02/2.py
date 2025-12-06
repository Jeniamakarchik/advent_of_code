import math


if __name__ == "__main__":
    with open("02/input.txt", "r") as f:
        line = f.readline().strip()

    ranges = []
    for pair in line.split(","):
        numbers = pair.split("-")
        ranges.append((int(numbers[0]), int(numbers[1])))

    invalid_ids = []
    for r1, r2 in ranges:
        print(f"Processing range: {r1}-{r2}")
        for number in range(r1, r2 + 1):
            invalid = False
            number_str = str(number)
            if number_str[0] not in number_str[1:]:
                continue
            
            number_len = len(number_str)
            dividors = [x for x in range(1, number_len // 2 + 1) if number_len % x == 0]
            for d in dividors[:: -1]:
                if all(number_str[:d] == number_str[d*i:d*(i+1)] for i in range(1, len(number_str)//d)):
                    invalid_ids.append(number)
                    invalid = True
                    print(f"Found invalid number: {number} with divisor {d}")
                    break
                
    print(sum(invalid_ids))
