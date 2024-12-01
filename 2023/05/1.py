from tqdm import tqdm
import re

# NOTE: Check reduce function for python

if __name__ == '__main__':
    with open('05/input.txt') as f:
        lines = f.readlines()

    # process mappings
    ind = 2
    source_to_destination = dict()
    while ind < len(lines):
        if re.match(r'^\d+ +\d+ \d+$', lines[ind]):
            destination, source, dist = lines[ind].split()
            for i in tqdm(range(int(dist))):
                source_to_destination[int(source) + i] = int(destination) + i
            print()
        elif lines[ind] == '\n':
            destinations = [source_to_destination[int(s)] if int(s) in source_to_destination else int(s) for s in sources ]
            print([f'{s} -> {d}' for s, d in zip(sources, destinations)])
            sources = destinations
        else:
            source_to_destination = dict()
        ind += 1

    print(min(sources))

    # # process seeds
    # sources = re.findall(r'\d+', lines[0])
    # print('Seeds:')
    # print(sources)

    # # process mappings
    # ind = 2
    # transitions = dict()
    # while ind < len(lines):
    #     if re.match(r'^\d+ +\d+ \d+$', lines[ind]):
    #         destination, source, dist = lines[ind].split()
    #         l_border = int(source)
    #         r_border = int(source) + int(dist)

    #         in_range = lambda x: l_border <= x < r_border
    #         for s in sources:
    #             if in_range(int(s)):
    #                 transitions[int(s)] = int(destination) + int(s) - l_border
            
    #     elif lines[ind] == '\n':
    #         print([f'{k} -> {v}' for k, v in transitions.items()])
    #         print()

    #         sources = [transitions[int(s)] if int(s) in transitions else int(s) for s in sources]
    #         transitions = dict()
    #     else:
    #         print(lines[ind].strip())
    #     ind += 1
    
    # print('Locations:')
    # print(sources)
    # print(min(sources))
