if __name__ == "__main__":
    with open("11/input.txt", "r") as f:
        numbers = [int(x) for x in f.read().split(" ")]
                   
    for i in range(25):
        j = 0
        while j < len(numbers):
            if numbers[j] == 0:
                numbers[j] = 1
                j += 1	
            elif len(str(numbers[j])) %2 == 0:
                length = len(str(numbers[j]))
                part_1 = int(str(numbers[j])[:length//2])
                part_2 = int(str(numbers[j])[length//2:])

                numbers[j] = part_1
                numbers.insert(j+1, part_2)

                j += 2
            else:
                numbers[j] *= 2024
                j += 1
    
    print(len(numbers))
