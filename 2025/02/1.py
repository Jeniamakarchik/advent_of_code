if __name__ == "__main__":
    with open("02/input.txt", "r") as f:
        line = f.readline().strip()

    ranges = []
    for pair in line.split(","):
        numbers = pair.split("-")
        print(numbers)
        ranges.append((int(numbers[0]), int(numbers[1])))

    invalid_ids = []
    for r1, r2 in ranges:
        for number in range(r1, r2 + 1):
            if len(str(number)) % 2 == 1:
               continue
            
            number_str = str(number)
            if number_str[:len(number_str)//2] == number_str[len(number_str)//2:]:
                invalid_ids.append(number)

    print(sum(invalid_ids))
