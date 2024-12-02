import numpy as np


def check_protocol(protocol):
    diff = np.array(protocol[1:]) - np.array(protocol[:-1])
    if np.max(np.abs(diff)) > 3 or np.min(np.abs(diff)) < 1:
        return False
        
    if np.all(diff < 0) or np.all(diff > 0):
        return True
    
    return False


if __name__ == "__main__":
    with open("02/input.txt", "r") as f:
        protocols = list()
        for line in f:
            protocols.append([int(d) for d in line.split()])

    safe_protocols = 0
    for protocol in protocols:
        if check_protocol(protocol):
            safe_protocols += 1
            continue
            
        for i in range(len(protocol)):
            if check_protocol(protocol[:i] + protocol[i+1:]):
                safe_protocols += 1
                break
            
    print(safe_protocols)
