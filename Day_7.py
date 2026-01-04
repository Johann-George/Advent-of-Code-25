def day_7_part_1():
    queue = set()
    total_splits = 0
    with open('Day_7_input.txt', 'r') as file:
        for line in file:
            if not queue:
                for index, c in enumerate(line):
                    if c == "^":
                        total_splits += 1
                        queue.add(index - 1)
                        queue.add(index + 1)
            else:
                for index in queue.copy():
                    if line[index] == "^":
                        total_splits += 1
                        queue.remove(index)
                        queue.add(index + 1)
                        queue.add(index - 1)
    return total_splits

print(day_7_part_1())