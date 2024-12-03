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

def checkSequence(vals): 
    currentValue: int = 0
    previousValue: int = 0
    status = ""
    variable = 0
    flag = "Safe"
    for i,v in enumerate(vals):
        currentValue = v
        if i == 0:
            previousValue = v
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
                flag = "Unsafe: Value is neither increasing or decreasing"
                return flag
            print(variable)
            if variable > 3:
                flag = "Unsafe: Variable is greater than 3"
                return flag
            else:
                previousValue = v         
        else:
            if status == "Increasing" and currentValue < previousValue:
                flag = "Unsafe: Was Increasing, now decreasing"
                return flag
            elif status == "Decreasing" and currentValue > previousValue: 
                flag = "Unsafe: Was Decreasing, now increasing"
                return flag
            elif currentValue == previousValue:
                flag = "Unsafe: Value remained the same"
                return flag
            else:
                variable = abs(currentValue - previousValue)   
                print(variable)       
                if variable > 3:
                    flag ="Unsafe: Variable greater than 3"
                    return flag
            if i == len(vals)-1:
                return flag
            else:
                previousValue = v
    
    return flag




with open(file_path, 'r') as file:
    for line in file:
        lines += 1
        result = ""
        values = line.strip().split(' ')  
        values = [int(item) for item in values]
        print(values)
        if len(values) == 0:
            break
        else:
            result = checkSequence(values)
            print(result)
            if result == "Safe":
                safeCount += 1
            else:
                for index, val in enumerate(values):
                    vals = values.copy()
                    del vals[index]
                    print(vals)
                    test = checkSequence(vals)
                    print(test)
                    if test == "Safe":
                        safeCount += 1
                        break
                    


print(safeCount)
print("")
