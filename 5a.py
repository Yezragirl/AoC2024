from typing import TextIO
import re
import math

# Initialize lists and variables to store updates, rules, and other intermediate data.
updates = []  # List to store updates parsed from the file.
correctUpdates = []  # List to store updates that pass all the rules.
rules = []  # List to store rules parsed from the file.
x = 0  # Variable to store the index of a rule element in updates.
y = 0  # Variable to store another index of a rule element in updates.
count = 0  # Counter to track the number of updates that pass all rules.
total = 0  # Accumulator to calculate the total sum of middle elements.
breakflag = False  # Flag to indicate if an update violates a rule and should be skipped.
file_path: str = 'C:/Users/jnp83/OneDrive/Advent of Code/input 5.txt'  # Path to the input file.

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

# Iterate over each update to check and process them based on the rules.
for i, update in enumerate(updates):
    updateCorrect = 0  # Flag to indicate if the update passes all the rules.
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
            updateCorrect = 1  # Mark the update as passing this rule.
        else:
            breakflag = True  # Mark the update as violating a rule.
            break  # Stop checking further rules for this update.
    if breakflag:  # If the update violated any rule:
        breakflag = False  # Reset the flag for the next update.
        continue  # Skip further processing for this update.
    if updateCorrect:  # If the update passes all the rules:
        count += 1  # Increment the count of correct updates.
        mid = math.ceil(len(update) / 2) - 1  # Find the middle index of the update.
        total += update[mid]  # Add the middle element to the total.
        correctUpdates.append(update)  # Add the update to the list of correct updates.

# Print the total sum of the middle elements of correct updates.
print(total)
