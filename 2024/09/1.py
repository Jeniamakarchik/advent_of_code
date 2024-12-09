if __name__ == "__main__":
    with open("09/input.txt", "r") as f:
        line = list(f.readline().strip())
        print(line)

    front_idx, back_idx = 0, len(line)-1
    current_pos = 0

    checksum = 0
    while front_idx <= back_idx:
        if front_idx % 2 == 0:
            current_label = front_idx // 2
            # calculate front
            for i in range(int(line[front_idx])):
                checksum += current_pos * current_label
                current_pos += 1
            front_idx += 1
        else:
            current_label = back_idx // 2
            if line[front_idx] < line[back_idx]:
                for i in range(int(line[front_idx])):
                    checksum += current_pos * current_label
                    current_pos += 1
                line[back_idx] = str(int(line[back_idx]) - int(line[front_idx]))
                front_idx += 1
            else:
                for i in range(int(line[back_idx])):
                    checksum += current_pos * current_label
                    current_pos += 1
                line[front_idx] = str(int(line[front_idx]) - int(line[back_idx]))
                back_idx -= 2

        print(f"front: {front_idx} back: {back_idx} checksum: {checksum} current_front_pos: {current_pos}")

    print(checksum)
