def find_password():
    default = 50
    count = 0
    with open("Day_1_input.txt", "r") as file:
        for line in file:
            line = line.strip()
            direction = line[0]
            steps = int(line[1:])

            for _ in range(steps):
                if direction == "L":
                    default = (default - 1) % 100
                else:
                    default = (default + 1) % 100
                if default == 0:
                    count += 1
    return count


print(find_password())