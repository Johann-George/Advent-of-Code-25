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
                        num = num / 2
                        if (i % (10 * num) == i // (10 * num)):
                            sum += i
                    else:
                        continue
    return sum

print(add_invalid_ids())