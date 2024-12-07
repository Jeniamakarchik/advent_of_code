def check_line(numbers, result):
    prev_results = [numbers[0]]
    for curr_number in numbers[1:]:
        curr_results = []
        for prev_result in prev_results:
            if prev_result + curr_number <= result:
                curr_results.append(prev_result + curr_number)
            if prev_result * curr_number <= result:
                curr_results.append(prev_result * curr_number)
        prev_results = curr_results

    return result in prev_results
    

if __name__ == "__main__":

    amount = 0
    with open("07/input.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            result, numbers = line.split(":")
            result = int(result)
            numbers = [int(n) for n in numbers.strip().split(" ")]

            print(result, numbers, " -> ", check_line(numbers, result))

            if check_line(numbers, result):
                amount += result
    
    print(amount)
