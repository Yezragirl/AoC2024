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
down3=''
up2=''
up3=''
left2=''
left3=''
right2=''
right3=''
leftup =''
leftup2 = ''
leftup3=''
rightup2=''
rightup3=''
leftdown2=''
leftdown3=''
leftdown =''
rightup = ''
rightdown =''
rightdown2=''
rightdown3=''
resultsbw = []
grid = []
row = ""
a = 0
horizontal = 0
horizontalBW = 0
vertical = 0
verticalBW = 0
diagonalDR = 0
diagonalUL = 0
diagonalUR = 0
diagonalDL = 0
word = "XMAS"
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


#find all instances of X, and S
for l,line in enumerate(grid):
    for i, letter in enumerate(line):
        if letter == word[0]:
            results.append([i,l])
            
for x,y in results:
    let = grid[y][x]
    
    try:
        left = grid[y][x-1]
    except:
        pass
    try:
        left2 = grid[y][x-2]
    except:
        pass
    try:
        left3 =  grid[y][x-3]
    except:
        pass
    try:
        right = grid[y][x+1]
    except IndexError:
        right = ''
    try:
        right2 = grid[y][x+2]
    except IndexError:
        right2 = ''
    try:
        right3 = grid[y][x+3]
    except IndexError:
        right3 = ''
    try:
        leftup = grid[y-1][x-1]
    except:
        pass
    try:
        leftup2 = grid[y-2][x-2]
    except:
        pass
    try:
        leftup3 = grid[y-3][x-3]
    except:
        pass
    try:
        leftdown = grid[y+1][x-1]
    except:
        pass
    try:
        leftdown2 = grid[y+2][x-2]
    except:
        pass
    try:
        leftdown3 = grid[y+3][x-3]
    except:
        pass
    try:
        rightup = grid[y-1][x+1]
    except IndexError:
        rightup = ''
    try:
        rightup2 = grid[y-2][x+2]
    except IndexError:
        rightup2 = ''
    try:
        rightup3 = grid[y-3][x+3]
    except IndexError:
        rightup3 = ''
    try:
        rightdown = grid[y+1][x+1]
    except IndexError:
        rightdown = ''
    try:
        rightdown2 = grid[y+2][x+2]
    except IndexError:
        rightdown2 = ''
    try:
        rightdown3 = grid[y+3][x+3]
    except IndexError:
        rightdown3 = ''
    try:
        up = grid[y-1][x]
    except:
        pass
    try:
        up2 = grid[y-2][x]
    except:
        pass
    try:
        up3 = grid[y-3][x]
        down = grid[y+1][x]
    except:
        pass
    try:
        down2 = grid[y+2][x]
    except:
        pass
    try:
        down3 = grid[y+3][x]
    except:
        pass

    #Firstletter
    test = word[1]
    test2 = word[2]
    test3 = word[3]
    try:
        if right == test and right2 == test2 and right3 == test3:
            horizontal += 1
        if x > 2 and left == test and left2 == test2 and left3 == test3:
            horizontalBW += 1
        if x > 2 and y > 2 and leftup == test and leftup2 == test2 and leftup3 == test3:
            diagonalUL += 1
        if x > 2 and leftdown == test and leftdown2 == test2 and leftdown3 == test3:
            diagonalDL += 1
        if y > 2 and rightup == test and rightup2 == test2 and rightup3 == test3:
            diagonalUR += 1
        if rightdown == test and rightdown2 == test2 and rightdown3 == test3:
            diagonalDR += 1
        if y > 2 and up == test and up2 == test2 and up3 == test3:
            verticalBW += 1
        if down == test and down2 == test2 and down3 == test3:
            vertical += 1
    except:
        continue



print("Horizontal", horizontal)
print("Horizontal Backwards", horizontalBW)
print("Vertical", vertical)
print("Vertical Backwards", verticalBW)
print("Diagonal Down Right", diagonalDR)
print("Diagonal Down Left", diagonalDL)
print("Diagonal Up Right", diagonalUR)
print("Diagonal Up Left", diagonalUL)

print("Total",sum([horizontal, horizontalBW, vertical, verticalBW, diagonalDR, diagonalUR, diagonalDL, diagonalUL]))
