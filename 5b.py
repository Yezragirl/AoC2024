from typing import TextIO
import re
import math

# Initialize lists and variables to store updates, rules, and other intermediate data.
updates = []  # List to store updates parsed from the file.
rules = []  # List to store rules parsed from the file.
x = 0  # Variable to store the index of a rule element in updates.
y = 0  # Variable to store another index of a rule element in updates.
count = 0  # Counter to track iterations while fixing an update.
total = 0  # Accumulator to calculate the total sum.
file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 5.txt'  # Path to the input file.

# Function to check if the rules are satisfied within an update.
def checkrules(update: list):
    for b, a in rules:  # Iterate over each rule (b, a).
        try:
            x = update.index(b)  # Find the index of element b in the update.
        except ValueError:
            continue  # If b is not in the update, skip to the next rule.
        try:
            y = update.index(a)  # Find the index of element a in the update.
        except ValueError:
            continue  # If a is not in the update, skip to the next rule.
        if x < y:  # Check if b appears before a in the update.
            continue  # If the rule is satisfied, continue to the next rule.
        else:
            return [b, a]  # Return the rule pair if the rule is violated.
    return "NA"  # Return "NA" if all rules are satisfied.

# Try to read the content of the input file.
try:
    with open(file_path, 'r') as file:
        text: str = file.read()  # Read the entire content of the file.
except FileNotFoundError:
    print(f'No File path found for : {file_path}')  # Print an error message if the file is not found.

# Reopen the file to process it line by line.
with open(file_path, 'r') as file:
    for line in file:  # Iterate through each line in the file.
        line = line.strip()  # Remove leading and trailing whitespace.
        if len(line) < 2:  # Skip lines that are too short to be valid.
            continue
        elif re.search("\|", line):  # Check if the line contains a pipe (|).
            line_list = line.split("|")  # Split the line into a list using the pipe as a delimiter.
            rulepair = [int(num) for num in line_list]  # Convert the list elements to integers.
            rules.append(rulepair)  # Add the parsed rule pair to the rules list.
        else:
            line_list = line.split(",")  # Split the line into a list using a comma as a delimiter.
            update = [int(num) for num in line_list]  # Convert the list elements to integers.
            updates.append(update)  # Add the parsed update to the updates list.

correct = False  # Initialize the flag to indicate if an update is correct.

# Iterate over each update to check and correct them based on the rules.
for i, update in enumerate(updates):
    correct = False  # Reset the correctness flag for each update.
    count = 0  # Reset the iteration count for each update.
    while correct == False:  # Repeat until the update is correct.
        count += 1  # Increment the iteration count.
        result = checkrules(update)  # Check the rules for the current update.
        if result == "NA":  # If all rules are satisfied:
            correct = True  # Mark the update as correct.
        else:
            x = update.index(result[0])  # Get the index of the first element of the violated rule.
            y = update.index(result[1])  # Get the index of the second element of the violated rule.
            num = update.pop(x)  # Remove the first element from the update.
            update.insert(y, num)  # Insert it before the second element to fix the order.
    if count > 1:  # If the update required corrections:
        mid = math.ceil(len(update) / 2) - 1  # Find the middle index of the corrected update.
        total += update[mid]  # Add the middle element to the total.

print(total)  # Print the final total sum of middle elements.
