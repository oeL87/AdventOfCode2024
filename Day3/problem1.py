import numpy as np
import re

def find_all_valid_mul(text):
    # Updated regex to match 'mul(x,y)' where x and y are integers (negative or positive)
    # allowing for other characters like '%&', '[', ']', etc. around the 'mul' pattern.
    pattern = r"mul\((-?\d+),\s*(-?\d+)\)"

    # Find all matches in the text using the updated regex pattern
    sum = 0
    for match in re.finditer(pattern, text):
        # Append the starting index of each match
        x = int(match.group(1))
        y = int(match.group(2))
        
        sum += x*y

    return sum

# num_pat = r"mul\((-?\d+),(-?\d+)\)$"
userin = input("input:\n")
sum = 0
while userin.lower() != 'done':
    sum += find_all_valid_mul(userin)
    userin = input()


# matches = []
# i=0

# for match in re.finditer(num_pat, userin):
#     matches.append(match.start)
print(sum)