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
        
        if not correct:
            subset_rules = {page:rules[page].intersection(set(pages)) for page in pages}
            subset_rules = [page[0] for page in sorted(subset_rules.items(), key=lambda x: len(x[1]), reverse=True)]
            pprint(subset_rules)

            acc_middle += subset_rules[len(subset_rules)//2]
    
    print(acc_middle)
