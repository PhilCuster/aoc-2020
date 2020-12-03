with open('day3\input.txt') as file:
    grid = [line.rstrip() for line in file]

width = len(grid[0])
# (Right, Down)
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
answer = 1

for slope in slopes:
    coords = [0,0]
    trees = 0

    while coords[1] < len(grid):
        if grid[coords[1]][coords[0]] == '#':
            trees += 1
        coords[1] += slope[1]
        coords[0] += slope[0]
        if coords[0] >= width:
            coords[0] -= width
    print("Numbers of trees hit: ", trees)
    answer = answer * trees

print("Final Answer: ", answer)
