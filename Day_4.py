def day_4_part_1():
    grid = []
    with open('Day_4_input.txt', 'r') as file:
        for line in file:
            grid.append(list(line.strip()))

    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "@":
                neighbout_count = 0

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if(0 <= ni < rows and 0 <= nj < cols):
                        if grid[ni][nj] == "@":
                            neighbout_count += 1

                if neighbout_count < 4:
                    count += 1
    return count

def day_4_part_2():
    grid = []
    with open('Day_4_input.txt', 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    total_count = 0
    while True:
        count = perform_analysis(grid)
        if(count == 0):
            break
        else:
            total_count += count
    return total_count

def perform_analysis(grid):
    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    count = 0
    rolls = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "@":
                neighbout_count = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if(0 <= ni < rows and 0 <= nj < cols):
                        if grid[ni][nj] == "@":
                            neighbout_count += 1

                if neighbout_count < 4:
                    count += 1
                    rolls.append([i,j])
    for val in rolls:
        grid[val[0]][val[1]] = "."
    return count




# print(day_4_part_1())
print(day_4_part_2())

