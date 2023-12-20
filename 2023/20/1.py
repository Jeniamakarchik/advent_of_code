from collections import deque, defaultdict
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

    low_impulses, high_impulses = 0, 0 
    for __name__ in range(n_iterations := 1000):
        impulses = deque([('broadcaster', False, '')])
        low_impulses += 1 # initial pulse is counted

        while impulses:
            name, signal, name_from = impulses.popleft()
            print(name_from, '->', name, 'high' if signal else 'low')
            if name == 'broadcaster':
                for output in modules[name]['outputs']:
                    impulses.append((output, signal, name))
                if signal:
                    high_impulses += len(modules[name]['outputs'])
                else:
                    low_impulses += len(modules[name]['outputs'])
            else:
                if 'on' in modules[name] and not signal:
                    if modules[name]['on']:
                        for output in modules[name]['outputs']:
                            impulses.append((output, False, name))
                            low_impulses += 1
                    else:
                        for output in modules[name]['outputs']:
                            impulses.append((output, True, name))
                            high_impulses += 1
                    modules[name]['on'] = not modules[name]['on']
                elif 'memory' in modules[name]:
                    modules[name]['memory'][name_from] = signal
                    if all(modules[name]['memory'].values()):
                        for output in modules[name]['outputs']:
                            impulses.append((output, False, name))
                            low_impulses += 1
                    else:
                        for output in modules[name]['outputs']:
                            impulses.append((output, True, name))
                            high_impulses += 1

    print(low_impulses * high_impulses)
