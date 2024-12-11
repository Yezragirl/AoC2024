from typing import TextIO
import re
import pprint as pp
import copy
file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 10.txt'

grid = []
workinggrid = []
trailhead_count = 0
trailhead_coords = []

def move(coords:list,grid: list,):
    next_locations = []
    x = coords[1]
    y = coords[0]
    value = grid[y][x]
    ylength = len(grid)
    xlength = len(grid[0])
    positions = [[y,x-1], [y-1,x], [y,x+1], [y+1,x]]
    for ny, nx in positions:
        if ny == -1 or nx == -1 or nx == xlength or ny == ylength:
            continue
        else:
            if grid[ny][nx] == value + 1:
                next_locations.append([ny, nx])
    return(next_locations)



try:
    with open(file_path, 'r',newline="\n") as file:
        text: str =file.read()
except FileNotFoundError:
    print(f'No File path found for : {file_path}')

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        grid.append(list(map(int, line)))
        
for y,line in enumerate(grid):
    for x,val in enumerate(line):
        if val == 0:
            trailhead_coords.append([y,x])
step_val = 0
pp.pprint(grid)
print(trailhead_coords)
next_steps = []
trail_ends = []
for trail in trailhead_coords:
    trail_ends.clear()
    trail_x = trail[1]
    trail_y = trail[0]
    next_steps.clear()
    step_val = 0
    workinggrid = copy.deepcopy(grid)
    next_steps = move([trail_y,trail_x],workinggrid)
    while step_val != 9:
        for step in next_steps:
            step_val = workinggrid[step[0]][step[1]]
            # print(step, step_val)
            if step_val == 9:
                trail_ends.append(str(step))
            next_steps.extend(s for s in move(step,workinggrid) if s not in next_steps)
    print(f"Trail Head: {trail_y}, {trail_x}")
    print(len(set(trail_ends)))
    trailhead_count += len(set(trail_ends))
print(trailhead_count)