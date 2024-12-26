import numpy as np
import re

def find_all_valid_mul(text, do_mul):
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_patt = r"do\(\)"
    dont_patt = r"don't\(\)"
    total = 0
    i = 0
    while i < len(text):
        # print(text[i:i+5])
        if re.match(do_patt, text[i:i+4]):
            do_mul = True
            i += 4
            # print("do found")
            continue
        # print(text[i:i+8])
        if re.match(dont_patt, text[i:i+7]):
            do_mul = False
            i += 7
            # print("dont found")
            continue
        if do_mul:
            match = re.match(mul_pattern, text[i:i+len("mul(123,123)")])
            if match:
                x = int(match.group(1))
                y = int(match.group(2))
                
                total += x*y
                i += match.end()
                continue
        i+=1
    
    return total, do_mul

userin = input("input:\n")
total = 0
do_mul = True
while userin.lower() != 'done':
    temp, do_mul = find_all_valid_mul(userin, do_mul)
    total += temp
    userin = input()
print(total)