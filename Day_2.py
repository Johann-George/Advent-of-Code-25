def add_invalid_ids():
    sum = 0
    with open('Day_2_input.txt', 'r') as file:
        for line in file:
            ranges = line.split(",")
            for numbers in ranges:
                nos = numbers.split("-")
                for i in range(int(nos[0]), int(nos[1])+1):
                    num = len(str(i))
                    if num % 2 == 0:
                        while num != 0:
                            string = str(i)[:num]
                            num = num // 2
                            if (string[:num] == string[num:]):
                                sum += i
                                break
                    else:
                        continue
    return sum

print(add_invalid_ids())