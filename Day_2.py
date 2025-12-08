def add_invalid_ids():
    sum = 0
    with open('Day_2_input.txt', 'r') as file:
        for line in file:
            ranges = line.split(",")
            for numbers in ranges:
                low, high = map(int, numbers.split("-"))
                for i in range(low, high + 1):
                    string = str(i)
                    num = len(string)
                    for k in range(1, num):
                        if num % k == 0:
                            pattern = string[:k]
                            if pattern * (num // k) == string:
                                sum += i
                                break
    return sum

print(add_invalid_ids())