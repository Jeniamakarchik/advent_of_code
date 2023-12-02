import re

color_blocks = {
    "red": 12,
    "green": 13,
    "blue": 14
}

game_pattern = r"Game (\d+):"
color_blocks_pattern = r"(\d+) (red|green|blue)"

if __name__ == "__main__":
    with (open("02/input.txt", "r")) as f:
        possible_games_number = 0
        for line in f.readlines():
            game_number = int(re.match(game_pattern, line).group(1))
            possible = True

            rounds = line.split(';')
            for round_str in rounds: 
                # Use re.findall to find all matches for color blocks in each round
                color_blocks_matches = re.findall(color_blocks_pattern, round_str)
                
                # Process each match for color blocks in the round
                for amount, color in color_blocks_matches:
                    if color_blocks[color] < int(amount):
                        possible = False
                        break

            if possible:
                possible_games_number += game_number

        print("Possible games: " + str(possible_games_number))
