from typing import TextIO
import re


file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 4.txt'
total = 0
lines = 0
results = []
left = ''
right =''
up = ''
down = ''
down2=''
up2=''
left2=''
right2=''
leftup =''
leftup2 = ''
rightup2=''
leftdown2=''
leftdown =''
rightup = ''
rightdown =''
rightdown2=''
resultsbw = []
grid = []
row = ""
a = 0
xs = 0
word = "MAS"
try:
    with open(file_path, 'r') as file:
        text: str =file.read()
except FileNotFoundError:
    print(f'No File path found for : {file_path}')

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        grid.append(line)
# print(grid)

# # Horizontal
# for line in grid:
#     count = re.findall(word,line)
#     horizontal += len(count)


# #Horizontal, backwards
# for line in grid:
#     count = re.findall(word[::-1] ,line)
#     horizontalBW += len(count)


#find all instances of A
for l,line in enumerate(grid):
    # print(line)
    for i, letter in enumerate(line):
        if letter == word[1]:
            results.append([i,l])
            
# print(len(results))

for x,y in results:
    if x < 1 or y < 1:
        continue

    let = grid[y][x]
    try:
        leftup = grid[y-1][x-1]
    except:
        pass
    try:
        leftdown = grid[y+1][x-1]
    except:
        pass
    try:
        rightup = grid[y-1][x+1]
    except IndexError:
        rightup = ''
    try:
        rightdown = grid[y+1][x+1]
    except IndexError:
        rightdown = ''

    # if y > 1:
    #     if x > 1:
    #         print(leftup, ".", rightup)
    #     else:
    #         print(".", ".", rightup)
    # else:
    #     print(".",".", ".")
    #     print(".",".", ".")

    # if x > 1:
    #     print(".", let, ".")
    #     print(leftdown, ".", rightdown)
    # else:
    #     print(".", let, ".")
    #     print(".", ".", rightdown)

    #Firstletter
    test = word[0]
    test2 = word[2]

    try:
        if ((leftup == test and rightdown == test2) or (leftup == test2 and rightdown == test)) and ((rightup == test and leftdown == test2) or (rightup == test2 and leftdown == test)):
            xs += 1
    except Exception as e:
        print(e)



print(xs)