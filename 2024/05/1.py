from collections import defaultdict
from pprint import pprint


if __name__ == "__main__":

    with open("05/input.txt", "r") as f:
        lines = f.readlines()
    
    rules = defaultdict(set)
    for idx, line in enumerate(lines):
        if line == "\n":
            break
        
        page_a, page_b = [int(x) for x in line.strip().split("|")]
        rules[page_a].add(page_b)


    # read printing sequences
    acc_middle = 0
    for line in lines[idx+1:]:
        pages = [int(x) for x in line.strip().split(",")]
        
        correct = True
        seen_pages = set()
        for page in pages:
            if rules[page].intersection(seen_pages):
                correct = False
                break
            seen_pages.add(page)
        
        if correct:
            acc_middle += pages[len(pages)//2]
    
    print(acc_middle)
