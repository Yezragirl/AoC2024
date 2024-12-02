from typing import TextIO

file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 2.txt'

try:
    with open(file_path, 'r') as file:
        text: str =file.read()
    print(text)
except FileNotFoundError:
    print(f'No File path found for : {file_path}')

    