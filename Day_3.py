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

def day_3_part_2_():
    total_joltage = 0
    with open("Day_3_input.txt", "r") as file:
        for line in file:
            digits = line.strip()
            stack = []

            to_remove = len(digits) - 12
            for d in digits:
                current = int(d)

                while stack and to_remove > 0 and stack[-1] < current:
                    stack.pop()
                    to_remove -= 1

                stack.append(current)
            if to_remove > 0:
                stack = stack[:-to_remove]

            stack = stack[:12]
            max_joltage = 0
            for digit in stack:
                max_joltage = max_joltage * 10 + digit

            total_joltage += max_joltage
    return total_joltage

print(day_3_part_2_())
print(day_3_part_1_())


