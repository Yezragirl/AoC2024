from typing import TextIO
import re
import pprint as pp
import copy
grid = []
ogGrid = []
workingGrid = []
list_of_antinodes = []
count_of_antinodes = 0
uniqueCharacters = set()
file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 8.txt'


def generate_combos(values):
    combos = [] 
    for i in range(len(values)):  
        for j in range(len(values)): 
            if i != j:  
                combos.append([values[i], values[j]])
    return combos


try:
    with open(file_path, 'r') as file:
        text: str =file.read()
except FileNotFoundError:
    print(f'No File path found for : {file_path}')

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        grid.append(list(line))
        
# pp.pprint(grid)
ogGrid = copy.deepcopy(grid)

for line in grid:
    for v in line:
        uniqueCharacters.add(v)
uniqueCharacters.remove(".")
# pp.pprint(uniqueCharacters)
locations = []
combos =[]
for character in uniqueCharacters:
    workingGrid = copy.deepcopy(ogGrid)
    locations.clear()
    combos.clear()
    for y,line in enumerate(workingGrid):
        for x,char in enumerate(line):
            if char == character:
                locations.append([y,x])

    if len(locations) > 2:
        combos = generate_combos(locations)
    else:
        combos = locations

    for i, combo in enumerate(combos):
        ylength = len(workingGrid)
        xlength = len(workingGrid[0])
        val1 = combo[0]
        val2 = combo[1]
        v1y= val1[0]
        v1x = val1[1]
        v2y = val2[0]
        v2x = val2[1]
        v3x = v1x + (v1x - v2x)
        v3y = v1y + (v1y - v2y)
        #if outside the grid
        if v3y <= -1 or v3x <= -1 or v3x >= xlength or v3y >= ylength:
            continue
        else: 
            list_of_antinodes.append([v3y,v3x])
        
uniqueAntinodes = [x for i, x in enumerate(list_of_antinodes) if x not in list_of_antinodes[:i]]
uniqueAntinodes.sort()
pp.pprint(uniqueAntinodes)
print(len(uniqueAntinodes))