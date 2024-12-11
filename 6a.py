from typing import TextIO
import re
import pprint
from collections import Counter

directions = {"left": "up",
                     "up": "right",
                     "right": "down",
                     "down": "left"}
grid = []
issue = "none"
row = []
x = 0
startingcoords = []
newcoords=[]
file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 6.txt'


def move(coords,direction,grid):
    path = 0
    x = coords[1]
    # print("x", x)
    y = coords[0]
    # print("y", y)
    match direction:
        case 'left':
            x2 = x-1
            y2 = y
        case 'right':
            x2 = x+1
            y2 = y
        case 'up':
            y2 = y-1
            x2 = x
        case 'down':
            y2 = y+1
            x2 = x
        case _:
            y2 = y
            x2 = x
    try:
        if grid[y2][x2] == '#':
            issue = "obstructed"
        else:
            if y == -1 or x == -1:
                issue = "off grid"
            else:
                issue = "none"
                coords = [y2,x2]
                grid[y2][x2] = "x"
    except IndexError:
        issue = "off grid"
    return(coords,direction,grid,issue)




try:
    with open(file_path, 'r') as file:
        text: str =file.read()
except FileNotFoundError:
    print(f'No File path found for : {file_path}')

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        grid.append(list(line))

# pprint.pprint(grid)
coords = []
#find coords of starting point
for y,l in enumerate(grid):
    try:
        x = l.index("^")
    except ValueError:
        continue
    else:
        coords = [y,x]
        # print(coords)

direction = "up"
while issue != 'off grid':
    if issue == "obstructed":
        direction = directions.get(direction)
        issue = "none"
    coords, direction, grid, issue= move(coords,direction,grid)
    print(coords, direction, issue)
    # pprint.pprint(grid)

count = 0
#count x's
for row in grid:
    count += row.count("x")

print(count)