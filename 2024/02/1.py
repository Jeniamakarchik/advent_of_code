import numpy as np


if __name__ == "__main__":
    with open("02/input.txt", "r") as f:
        protocols = list()
        for line in f:
            protocols.append([int(d) for d in line.split()])

    safe_protocol_counts = 0
    for protocol in protocols:
        protocol = np.array(protocol[1:]) - np.array(protocol[:-1])
        if np.max(np.abs(protocol)) > 3 or np.min(np.abs(protocol)) < 1:
            continue
        
        if np.all(protocol < 0) or np.all(protocol > 0):
            safe_protocol_counts += 1 
            
    print(safe_protocol_counts)
