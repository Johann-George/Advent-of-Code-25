def day_5_part_1():
    ranges = []
    flag = 0
    fresh = 0
    with open('Day_5_input.txt', 'r') as file:
        for line in file:
            if not line.strip():
                flag = 1
                continue
            if flag == 1:
                for val in ranges:
                    no = int(line)
                    if(int(val[0]) <= no and no <= int(val[1])):
                        fresh += 1
                        break
            else:
                ranges.append(list((line.strip()).split('-')))
    
    return fresh

def day_5_part_2():
    ranges = []
    with open('Day_5_input.txt', 'r') as file:
        for line in file:
            if not line.strip():
                break
            ranges.append([int(x) for x in line.strip().split('-')])
    ranges.sort(key=lambda x : x[0])
    total = 0
    current_start, current_end = ranges[0]
    for start, end in ranges[1:]:
        if(start <= current_end):
            current_end = max(current_end, end)
        else:
            total += current_end - current_start + 1
            current_start, current_end = start, end

    total += current_end - current_start + 1
    return total


# print(day_5_part_1())
print(day_5_part_2())
