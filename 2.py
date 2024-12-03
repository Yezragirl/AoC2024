from typing import TextIO

file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 2.txt'
safeCount: int = 0
currentValue: int = 0
previousValue: int = 0
status = ""
variable = 0
lines = 0
errors = 0
flag = "Safe"
try:
    with open(file_path, 'r') as file:
        text: str =file.read()
    # print(text)
except FileNotFoundError:
    print(f'No File path found for : {file_path}')

with open(file_path, 'r') as file:
    for line in file:
        lines += 1
        errors = 0
        values = line.strip().split(' ')  
        values = [int(item) for item in values]
        print(values)
        if len(values) == 0:
            break
        else:
            for i,v in enumerate(values):
                currentValue = v
                if i == 0:
                    previousValue = v
                    continue
                elif i == 1:
                    if currentValue > previousValue:
                        print("Increasing")
                        status = "Increasing"
                        variable = abs(currentValue - previousValue)
                    elif currentValue < previousValue:
                        print("Decreasing")
                        status = "Decreasing"
                        variable = abs(currentValue - previousValue)
                    else:
                        print("Unsafe: Value is neither increasing or decreasing")
                        break
                    print(variable)
                    if variable > 3:
                        print("Unsafe: Variable is greater than 3")
                        break
                    else:
                        previousValue = v         
                else:
                    if status == "Increasing" and currentValue < previousValue:
                        print("Unsafe: Was Increasing, now decreasing")
                        break
                    elif status == "Decreasing" and currentValue > previousValue: 
                        print("Unsafe: Was Decreasing, now increasing")
                        break
                    elif currentValue == previousValue:
                        print("Unsafe: Value remained the same")
                        break
                    else:
                        variable = abs(currentValue - previousValue)   
                        print(variable)       
                        if variable > 3:
                            print("Unsafe: Variable greater than 3")
                            break
                    if i == len(values)-1:
                        print("Safe")
                        safeCount += 1
                    else:
                        previousValue = v

print(safeCount)
print("")
