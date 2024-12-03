from typing import TextIO
import re

file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 3.txt'
total = 0
a = 0
b = 0
exe = "Enabled"
try:
    with open(file_path, 'r') as file:
        text: str =file.read()
except FileNotFoundError:
    print(f'No File path found for : {file_path}')

with open(file_path, 'r') as file:
    for line in file:
        dos = re.findall("do\(\)|don\'t\(\)|mul\(\d{1,3}\,\d{1,3}\)",line)
        # print(dos)
        for do in dos:
            if do == "do()":
                exe = "Enabled"
            elif do == "don't()":
                exe = "Disabled"
            captures = re.findall("(mul\(\d{1,3}\,\d{1,3}\))",do)
            for value in captures:
                inputs = re.findall("\d{1,3}",value)
                a = int(inputs[0])
                b = int(inputs[1])
                if exe == "Enabled":
                    total += (a*b)
        
print(total)