from collections import Counter


if __name__ == "__main__":
    with open("01/input.txt", "r") as f:
        right_array, left_array = [], []
        for line in f:
            right, left = line.split()
            right_array.append(int(right))
            left_array.append(int(left))

    result = 0
    counts = Counter(right_array)
    for number in left_array:
        # print(number, " -> ", counts[number])
        result += counts[number] * number
    
    print(result)
