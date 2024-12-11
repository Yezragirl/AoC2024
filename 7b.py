from typing import TextIO
import re
import pprint
import copy
from collections import Counter
file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 7.txt'
formulas = []
maths = ["+", "*", "||"]
calc_list = []
operator = ""
sum_of_calculable = 0

def generate_ops_combos(values, operators=None, current_combo=None, combos=None):
    if operators is None:
        operators = ['+', '*', "||"]
    if current_combo is None:
        current_combo = [] 
    if combos is None:
        combos = []  

    if len(current_combo) == len(values) - 1:
        combos.append(current_combo[:])
        return combos

    for operator in operators:
        current_combo.append(operator)
        generate_ops_combos(values, operators, current_combo, combos)
        current_combo.pop()

    return combos


def custom_eval(values:list):
    newVals = [str(val) for val in values]
    # print(newVals)
    firstWave = newVals[0:3]
    calculate = "".join([str(val) for val in firstWave if val != "||"])
    calculate = eval(calculate)
    del newVals[0:3]
    while len(newVals)>0:
        nextWave = newVals[0:2]
        nextWave.insert(0,str(calculate))
        calculate = "".join([str(val) for val in nextWave if val != "||"])
        calculate = eval(calculate)
        del newVals[0:2]
            
    return calculate
        
try:
    with open(file_path, 'r') as file:
        text: str =file.read()
except FileNotFoundError:
    print(f'No File path found for : {file_path}')

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split(":")
        line[1] = line[1].strip()
        line[1] = line[1].split(" ")
        print(line)
        formulas.append({"solution": line[0],"values": line[1]})
        # print(formulas)
        
for formula in formulas:
    solved = False
    vals = formula.get("values") 
    sol = int(formula.get("solution"))
    calculated = 0
    ops_combos = generate_ops_combos(vals)
    for combo in ops_combos:
        calc_list.clear()
        for i,v in enumerate(vals):
            if i == 0:
                calc_list.append(v)
            else:
                op = combo.pop()
                calc_list.append(op)
                calc_list.append(v)
        calculated = custom_eval(calc_list)
        if calculated == sol:
            solved = True
            sum_of_calculable += sol
            break
    if solved == True: 
        print("Solved")
        continue
    print("Not Solvable")    
print(sum_of_calculable)