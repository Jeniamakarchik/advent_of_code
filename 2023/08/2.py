import re
import math


def find_finish(map_nodes, curr_node, instruction):
    idx = 0
    while curr_node[-1] != 'Z':
        direction = idx % len(instruction)
        curr_node = map_nodes[curr_node][0 if instruction[direction] == 'L' else 1]
        idx += 1

    return idx


if __name__ == "__main__":
    with open("08/input.txt", "r") as f:
        lines = f.readlines()
        instruction = lines[0].strip()

        start_nodes = []
        finish_nodes = []

        map_nodes = {}
        for line in lines[2:]:
            node, turn_l, turn_r = re.findall(r'\w+', line.strip())
            map_nodes[node] = (turn_l, turn_r)

            if node[-1] == 'A':
                start_nodes.append(node)
            # elif node[-1] == 'Z':
            #     finish_nodes.append(node)
    
    turns = [find_finish(map_nodes, node, instruction) for node in start_nodes]
    print(math.lcm(*turns))
