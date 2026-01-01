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

print(day_4_part_1())

