from typing import TextIO
import re
import pprint as pp
import copy
file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 9.txt'

parsedText = ''


def parseText(text):
    type_data = 'data'
    id = 0
    pt= []
    for i,num in enumerate(text):
        if type_data == 'data':
            if num == 0:
                continue
            elif num == 1:
                pt.append(num)
            else:
                for n in range(0,int(num)):
                    pt.append(id)
            id += 1
            type_data = "free"
        else:
            if num == 0:
                continue
            elif num == 1:
                pt.append(".")
            else:
                for n in range(0,int(num)):
                    pt.append(".")
            type_data = "data"
    return pt        

try:
    with open(file_path, 'r',newline="\n") as file:
        text: str =file.read()
except FileNotFoundError:
    print(f'No File path found for : {file_path}')



text = text.strip()
newText = parseText(text)
print(newText)

while True:
    last_data = -1
    for i in range(len(newText) - 1, -1, -1): 
        if newText[i] != '.':
            last_data = i
            break
    for i in range(len(newText) -1):
        if newText[i] == ".":
            first_dot = i
            break
    if last_data != -1:
        if first_dot < last_data:
            newText[first_dot] = newText[last_data]
            newText[last_data] = '.'
        else:
            break
print(newText)
checksum = 0        
for i,num in enumerate(newText):
    if num != ".":
        print(i, "*" ,num)
        val = i * (int(num))
        checksum += val
    else:
        break
print(checksum)
print("end")