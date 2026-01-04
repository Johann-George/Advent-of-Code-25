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

def day_6_part_2():
    numbers = []
    total = 0
    with open('Day_6_input.txt', 'r') as file:
        numbers = [list(line.rstrip("\n")) for line in file]
    num_arr = []
    temp = ""
    for i in range (len(numbers[0]) - 1, -1, -1):
        for nums in numbers:
            if nums[i] == " ":
                continue
            elif nums[i] == "+" or nums[i] == "*":
                if nums[i] == "+":
                    sum = 0
                    num_arr.append(temp)
                    temp = ""
                    for num in num_arr:
                        sum += int(num)
                    print(sum)
                    total += sum
                else:
                    mul = 1
                    num_arr.append(temp)
                    for num in num_arr:
                        mul *= int(num)
                    print(mul)
                    total += mul
                num_arr = []
                temp = ""
            else:
                temp += nums[i] 
        if temp:
            num_arr.append(temp)
            temp = ""
    return total

print(day_6_part_2())
print(day_6_part_1())
        