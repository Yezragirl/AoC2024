from typing import TextIO
import re
import pprint as pp
import copy
file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 10.txt'

grid = []
workinggrid = []
trailhead_count = 0
trailhead_coords = []
count_of_trail_ends = 0

def move(coords:list,grid: list,):
    locations = []
    x = coords[1]
    y = coords[0]
    locations.append([y,x])
    value = grid[y][x]
    ylength = len(grid)
    xlength = len(grid[0])
    positions = [[y,x-1], [y-1,x], [y,x+1], [y+1,x]]
    for ny, nx in positions:
        if ny == -1 or nx == -1 or nx == xlength or ny == ylength:
            continue
        else:
            if grid[ny][nx] != value + 1:
                continue
            elif grid[ny][nx] == 9:
                locations.append([ny,nx])
                trail_ends.append(f"{ny},{nx}")
            else:
                locations.append([ny,nx])
                move([ny,nx], workinggrid)
            
    print(f"{locations=}")
    return(trail_ends)



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
# print(trailhead_coords)
next_steps = []
trails = []
trail_ends = []
for trailhead in trailhead_coords:
    rounds = 1
    trail_ends.clear()
    trail_x = trailhead[1]
    trail_y = trailhead[0]
    next_steps.clear()
    step_val = 0
    workinggrid = copy.deepcopy(grid)

    
    trail_ends = move([trail_y,trail_x],workinggrid)
    print(len(trail_ends), trail_ends)
    count_of_trail_ends += len(trail_ends)
print(count_of_trail_ends)