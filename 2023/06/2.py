import re
import numpy as np


if __name__ == '__main__':
    with open('06/input.txt') as file:
        data = file.read().split('\n')
        time = int("".join(re.split(r' +', data[0].split(':')[1].strip())))
        distance = int("".join(re.split(r' +', data[1].split(':')[1].strip())))

    print('time:', time)
    print('distance:', distance)

    calculate_distance = lambda x: x * (time - x)
    results = np.array([calculate_distance(t) for t in range(time+1)])

    wins = np.sum(results > int(distance))
    print(results, 'record:', distance, 'wins:', wins)
    
    print('Wins:', wins)
