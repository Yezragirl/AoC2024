from typing import TextIO

file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 1.txt'

try:
    with open(file_path, 'r') as file:
        text: str =file.read()
    print(text)
except FileNotFoundError:
    print(f'No File path found for : {file_path}')

def get_two_lists_from_file(file_path):
    list1 = []
    list2 = []

    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split('   ')  
            if len(values) == 2:
                list1.append(int(values[0]))
                list2.append(int(values[1]))

    return list1, list2

# Example usage
list1, list2 = get_two_lists_from_file(file_path)

print("List 1:", list1)
print("List 2:", list2)

lista = sorted(list1)
listb = sorted(list2)
# print(lista)
# print(listb)
listd = []
listc = []
for i in range(listb.__len__()):
    listd.append(abs(lista[i]-listb[i]))


print(listd)
print(sum(listd))

for i in range(listb.__len__()):
    print(lista[i]) 
    print(listb.count(lista[i]))
    c = lista[i] * listb.count(lista[i])
    listc.append(c)
    
print(listc)
print(sum(listc))