import numpy as np


def extrapolate_line(data):
    arr = np.array(data)
    curr_beg = 0
    
    while curr_beg < (len(data) - 1) and np.any(arr[curr_beg:]):
        print(arr)
        arr[(curr_beg + 1):] = np.diff(arr[curr_beg:])
        curr_beg += 1

    print(" ".join([str(el) for el in arr]), 'curr_beg =', curr_beg, end=" ")
    return np.sum(arr[:curr_beg:2]) - np.sum(arr[1:curr_beg:2])


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
