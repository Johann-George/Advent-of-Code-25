def day_3_part_1():
    total_joltage = 0
    with open("Day_3_input.txt", "r") as file:
        for line in file:
            print(line)
            max_val = -1
            max_val2 = -1
            i = 0
            while line[i] != '\n':
                num = int(line[i])
                if(num > max_val2 or num > max_val):
                    if max_val > max_val2:
                        max_val2 = num
                    else:
                        max_val = max_val2
                        max_val2 = num
                i += 1
            print("max_val=", max_val, "max_val2=", max_val2)
            total_joltage += max_val*10 + max_val2
    return total_joltage

print(day_3_part_1())


