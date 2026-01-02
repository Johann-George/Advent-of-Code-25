def day_6_part_1():
    numbers = []
    res = 0
    with open('Day_6_input.txt', 'r') as file:
        for line in file:
            numbers.append(line.strip().split())
    i = 0
    for op in numbers[-1]:
        if op == "+":
            sum = 0
            for val in numbers[0:-1]:
                sum += int(val[i])
            res += sum
        else:
            mul = 1
            for val in numbers[0:-1]:
                mul *= int(val[i])
            res += mul
        i += 1
    return res

print(day_6_part_1())
        