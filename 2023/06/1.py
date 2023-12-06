import re
import numpy as np

# equation: distance = time_hold * (time_race - time_hold)

if __name__ == '__main__':
    with open('06/input.txt') as file:
        data = file.read().split('\n')
        times = [int(t) for t in re.split(r' +', data[0].split(':')[1].strip())]
        distances = [int(d) for d in re.split(r' +', data[1].split(':')[1].strip())]

        print('times:', times)
        print('distances:', distances)
    
    total_wins = 1
    for time, distance in zip(times, distances ):
        calculate_distance = lambda x: x * (time - x)
        results = np.array([calculate_distance(t) for t in range(time+1)])

        wins = np.sum(results > int(distance))
        print(results, 'record:', distance, 'wins:', wins)
        total_wins *= wins
    
    print('Total wins:', total_wins)
    