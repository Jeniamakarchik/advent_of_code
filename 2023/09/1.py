import numpy as np


def extrapolate_line(data):
    arr = np.array(data)
    curr_end = len(data) - 1
    
    while curr_end > 0 and np.any(arr[:curr_end]):
        # print(arr)
        arr[:curr_end] = np.diff(arr[:(curr_end+1)])
        curr_end -= 1

    print(" ".join([str(el) for el in arr]), 'curr_end=', curr_end, end=" ")
    return np.sum(arr[curr_end:])


if __name__ == "__main__":
    with open("09/input.txt", "r") as f:
        lines = f.readlines()
        inputs = [[int(el) for  el in line.strip().split()] for line in lines]
    
    # NOTE: can be done via processing a matrix
    total_extrapolation = 0
    for inp in inputs:
        ext = extrapolate_line(inp)
        print("extrapolation", ext)
        total_extrapolation += ext
    
    print("Total extrapolation:", total_extrapolation)
