import copy

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

def day_7_part_2():
    with open('Day_7_input.txt', 'r') as file:
        data = [[l for l in line] for line in file]
    for col in range(len(data[0])):
        if data[0][col] == 'S':
            data[1][col] = '|'

    for col in range(len(data[1])):
        if data[1][col] == '|':
            beam = col
            break
    
    return dfs(data[1:], 0 , beam)

MEM = {}

def dfs(currState, currLine, beam):

    if(currLine, beam) in MEM:
        return MEM[(currLine, beam)]

    if currLine == len(currState) - 2:
        return 1
    
    nextLine = currLine + 1
    if currState[nextLine][beam] == '^':
        nextState1 = copy.deepcopy(currState) 
        nextState2 = copy.deepcopy(currState)
        nextState1[nextLine][beam - 1] = '|'
        nextState2[nextLine][beam + 1] = '|'

        ans = dfs(nextState1, nextLine, beam-1) + dfs(nextState2, nextLine, beam+1)

    else:
        currState[nextLine][beam] = '|'
        ans = dfs(currState, nextLine, beam)

    MEM[(currLine, beam)] = ans
    return ans

print(day_7_part_2())