from typing import TextIO
import re
import pprint as pp
import copy
file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 9.txt'

parsedText = ''

def find_subset(larger_set, subset):
    subset_len = len(subset)
    for i in range(len(larger_set) - subset_len + 1):
        if larger_set[i:i + subset_len] == subset:
            return i
    return False



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



data_package = []
exceptionList = ['.']
while newText[0] not in exceptionList:
    last_data_index = []
    last_data = ''
    first_data_index = []
    first_data = ''
    for i in range(len(newText) - 1, -1, -1): 
        if newText[i] not in exceptionList:
            last_data_index = i
            last_data = newText[i]
            break
    for j in range(len(newText) -1):
        if newText[j] == last_data:
            first_data_index = j
            break
    if j == len(newText)-1:
        data_package = newText[j:]
    else:        
        data_package = newText[j:i+1]

    free_package = copy.deepcopy(data_package)
    for i,val in enumerate(free_package):
        free_package.pop()
        free_package.insert(0,".")
        
    print(data_package)
    print(free_package)

    starting_index_free = find_subset(newText, free_package)
    if starting_index_free and starting_index_free < first_data_index:
        for n in range(len(free_package)):
            del newText[starting_index_free]
        for n in range(len(data_package)):
            newText.insert(starting_index_free,data_package[n-1])    
        for n in range(len(data_package)):
            del newText[first_data_index]
        for n in range(len(free_package)):
            newText.insert(first_data_index,free_package[n-1])  
        print(newText)
    exceptionList.append(data_package[0])
    # for i in range(len(newText) -1):
    #     if newText[i] == ".":
    #         first_dot = i
    #         break
    # if last_data != -1:
    #     if first_dot < last_data:
    #         newText[first_dot] = newText[last_data]
    #         newText[last_data] = '.'
    #     else:
    #         break
print(newText)





checksum = 0        
for i,num in enumerate(newText):
    if num != ".":
        print(i, "*" ,num)
        val = i * (int(num))
        checksum += val
print(checksum)
print("end")