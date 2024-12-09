if __name__ == "__main__":
    with open("09/input.txt", "r") as f:
        line = list(f.readline().strip())

    disc = [(value // 2 if value % 2 == 0 else 0, int(size))  for value, size in enumerate(line)]
    print(disc)

    for back_idx in range(len(disc))[::-1]:
        # going through the disc from the front and checking all slots as new parts are freed
        for front_idx in range(1, back_idx):
            back_data, back_size = disc[back_idx]
            front_data, front_size = disc[front_idx]

            if back_data !=0 and front_data == 0 and back_size <= front_size:
                disc[back_idx] = (0, back_size)
                disc[front_idx] = (0, front_size - back_size)
                disc.insert(front_idx, (back_data, back_size))

    print(disc)

    checksum, curr_pos = 0, 0
    for idx, (value, size) in enumerate(disc):
        checksum += sum([value * (curr_pos + i) for i in range(size)])
        curr_pos += size
    print(checksum)
