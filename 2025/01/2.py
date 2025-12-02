if __name__ == "__main__":
    with open("01/input.txt", "r") as f:
        lines = f.readlines()

    current_positition = 50
    times_pointed_to_zero = 0
    for line in lines:
        direction, turn = line[0], int(line[1:])

        # remove all cycles
        points_to_zero = turn // 100
        turn = turn % 100
        
        if direction == "L":
            turn = 100 - turn

        prev_position = current_positition
        current_positition += turn
        current_position_turn = current_positition // 100
        current_positition %= 100

        if current_position_turn == 1:
            if current_positition == 0:
                points_to_zero = points_to_zero + 1
            elif direction == 'R':
                points_to_zero = points_to_zero + 1
        else:
            if direction == 'L' and prev_position != 0:
                points_to_zero = points_to_zero + 1
            
        print(f'Turn to {line}\t-> pos {current_positition}')

        times_pointed_to_zero = times_pointed_to_zero + points_to_zero
        print(f'\t{points_to_zero}')

    print(f'Actual password: {times_pointed_to_zero}')
