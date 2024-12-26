import numpy as np

def intake(userin):
    row = []
    # userin = input()
    try:
        nums = list(map(int, userin.split()))
        arr = np.array(nums)
        return arr
    except ValueError:
        print("Invalid input! Please enter space-separated integers.")
        return None
    
def increase(arr):
    prev = arr[0]
    for i, a in enumerate(arr):
        if i == 0:
            continue
        if a <= prev:
            return False
        elif a - prev > 3:
            # print(f'{a=}\n{prev=}')
            return False
        prev = a
    return True

def decrease(arr):
    prev = arr[0]
    for i, a in enumerate(arr):
        if i == 0:
            continue
        if a >= prev:
            return False
        elif prev - a > 3:
            # print(f'{prev-a=}')
            return False
        prev = a
    return True

safe = 0
while True:
    userin = input()
    # print(userin)
    if userin.lower() == 'done':
        break
    arr = intake(userin)
    if increase(arr) or decrease(arr):
        safe += 1
    # print(increase(arr))
    # print(decrease(arr))

print(safe)