import re

def find_finish(map_nodes, curr_node, finish, instruction):
    idx = 0
    while curr_node != finish:
        direction = idx % len(instruction)
        curr_node = map_nodes[curr_node][0 if instruction[direction] == 'L' else 1]
        idx += 1

    return idx


if __name__ == "__main__":
    with open("08/input.txt", "r") as f:
        lines = f.readlines()
        instruction = lines[0].strip()

        map_nodes = {}
        for line in lines[2:]:
            node, turn_l, turn_r = re.findall(r'\w+', line.strip())
            map_nodes[node] = (turn_l, turn_r)

    curr_node = 'AAA'
    end_node = 'ZZZ'

    turns = find_finish(map_nodes, curr_node, end_node, instruction)

    print(turns)
        