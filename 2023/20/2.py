from collections import deque, defaultdict
from math import lcm
from pprint import pprint

if __name__ == "__main__":
    modules = defaultdict(dict)

    with open("20/input.txt", "r") as f:
        for line in f.readlines():
            name, outputs = line.strip().split("->")
            if '%' in name:
                name = name[1:]
                modules[name.strip()]['on'] = False
            if '&' in name:
                name = name[1:]
                modules[name.strip()]['memory'] = dict() if 'inputs' not in modules[name.strip()] else dict({n: False for n in modules[name.strip()]['inputs']})

            modules[name.strip()]['outputs'] = outputs.strip().split(", ")
            for output in outputs.strip().split(", "):
                if 'inputs' in modules[output.strip()]:
                    modules[output.strip()]['inputs'].append(name.strip())
                else:
                    modules[output.strip()]['inputs'] = [name.strip()]

                if 'memory' in modules[output.strip()]:
                    modules[output.strip()]['memory'][name.strip()] = False # False for low signal

    pprint(modules)

    cumm_button_turns = 0
    rx_turned = False
    
    cycles = dict()

    while not rx_turned and len(cycles) < 4:
        impulses = deque([('broadcaster', False, '')])
        cumm_button_turns += 1

        while impulses:
            name, signal, name_from = impulses.popleft()

            if name == 'rx' and not signal and not rx_turned:
                rx_turned = True
                break

            if name == 'gf' and signal:
                print('Button:', cumm_button_turns, ',', name_from, '->', name, 'high' if signal else 'low')
                if name_from not in cycles:
                    cycles[name_from] = cumm_button_turns

            if name == 'broadcaster':
                for output in modules[name]['outputs']:
                    impulses.append((output, signal, name))
            else:
                if 'on' in modules[name] and not signal:
                    if modules[name]['on']:
                        for output in modules[name]['outputs']:
                            impulses.append((output, False, name))
                    else:
                        for output in modules[name]['outputs']:
                            impulses.append((output, True, name))
                    modules[name]['on'] = not modules[name]['on']
                elif 'memory' in modules[name]:
                    modules[name]['memory'][name_from] = signal
                    if all(modules[name]['memory'].values()):
                        for output in modules[name]['outputs']:
                            impulses.append((output, False, name))
                    else:
                        for output in modules[name]['outputs']:
                            impulses.append((output, True, name))

    print(lcm(*cycles.values()))
