import re

max_per_round = {
    "red": 0,
    "green": 0,
    "blue": 0
}

color_blocks_pattern = r"(\d+) (red|green|blue)"

if __name__ == "__main__":
    with (open("02/input.txt", "r")) as f:
        game_power = 0
        for line in f.readlines():

            rounds = line.split(';')
            for round_str in rounds: 
                # Use re.findall to find all matches for color blocks in each round
                color_blocks_matches = re.findall(color_blocks_pattern, round_str)
                
                # Process each match for color blocks in the round
                for amount, color in color_blocks_matches:
                    if max_per_round[color] < int(amount):
                        max_per_round[color] = int(amount)

            power = 1
            for color, value in max_per_round.items():
                power *= value
                max_per_round[color] = 0
            
            game_power += power

            print(line, "->", power)

        print("Game power: " + str(game_power))
