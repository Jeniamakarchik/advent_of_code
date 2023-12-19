import re


def process_workflows(workflows):
    workflows_mapping = dict()
    for workflow in workflows:
        name, rules = workflow.strip().split("{")
        workflows_mapping[name] = rules[:-1].split(',')
    return workflows_mapping


def process_rule(rule):
    pass


if __name__ == "__main__":
    with open("19/input.txt", "r") as f:
        lines = f.read()
        workflows = lines.split("\n\n")[0].strip().split("\n")
        parts_list = lines.split("\n\n")[1].strip().split("\n")

    workflows_mapping = process_workflows(workflows)

    total_sum = 0
    for parts in parts_list:
        for part in re.findall(r"([a-z]+=[0-9]+)", parts):
            exec(part)
        
        res = 'in'
        while res not in ['A', 'R']:
            workflow = workflows_mapping[res]
            for proc in workflow:
                if ':' in proc:
                    rule, name = proc.split(':')
                    if eval(rule):
                        res = name
                        break
                else:
                    res = proc

        if res == 'A':
            total_sum += (x + m + a + s)

        print(parts, '->', res, '->', (x + m + a + s))

    print(total_sum)
