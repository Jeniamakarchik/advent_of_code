if __name__ == "__main__":
    with open("01/input.txt", "r") as f:
        lines = f.readlines()

    current_postition = 50
    times_pointed_to_zero = 0
    for line in lines:
        direction, turn = line[0], int(line[1:])

        turn %= 100
        if direction == "L":
            turn = 100 - turn
        
        current_postition += turn
        current_postition %= 100

        print(f'Turn to {line} -> pos {current_postition}')

        if current_postition == 0:
            times_pointed_to_zero += 1

    print(f'Actual password: {times_pointed_to_zero}')
