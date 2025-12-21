def day_3_part_1_():
    total_joltage = 0
    with open("Day_3_input.txt", "r") as file:
        for line in file:
            max_joltage = 0
            for i in range(0, len(line)-2):
                for j in range(i+1, len(line)-1):
                    num = int(line[i]) * 10 + int(line[j])
                    if (num > max_joltage):
                        max_joltage = num
            total_joltage += max_joltage

    return total_joltage


print(day_3_part_1_())


