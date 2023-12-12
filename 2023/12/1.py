def count_combinations(line, groups, curr_group_size=0):
    if len(line) == 0:
        return int(len(groups) == 0 and curr_group_size == 0) # we closed all the groups and we don't have any open group

    num_combinations = 0
    curr_el = ['.', '#'] if line[0] == '?' else [line[0]]
    for el in curr_el:
        if el == '#':
            if groups:
                # we always continue to get a group here
                num_combinations += count_combinations(line[1:], groups, curr_group_size + 1)
        elif el == '.':
            if curr_group_size > 0:
                if curr_group_size == groups[0]:
                    # we can close a group here if it is open
                    num_combinations += count_combinations(line[1:], groups[1:])
            else:
                # we can just go further
                num_combinations += count_combinations(line[1:], groups)

    return num_combinations

if __name__ == "__main__":
    with open("2023/12/input.txt", "r") as f:
        springs, sequential_groups = [], []
        for line in f.readlines():
            parts = line.strip().split(" ")
            springs.append(parts[0] + '.') # add '.' at the end to close all the groups
            sequential_groups.append([int(group) for group in parts[1].split(",")])  
    
    print(sum([count_combinations(spring, group) for spring, group in zip(springs, sequential_groups)]))
