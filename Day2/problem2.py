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
    # problem_count = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
        if arr[i] - arr[i-1] > 3:
            return False
    return True

def decrease(arr):
    # problem_count = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            return False
        if arr[i-1] - arr[i] > 3:
            return False
    return True

def can_be_made_safe(arr):
    for i in range(len(arr)):
        temp_arr = np.delete(arr, i)  # Try removing one element at position i
        if increase(temp_arr) or decrease(temp_arr):
            return True
    return False

def check_safe(arr):
    # Check if the report is already safe (either increasing or decreasing)
    if increase(arr) or decrease(arr):
        return True
    # Otherwise, check if we can remove one element to make it safe
    return can_be_made_safe(arr)

safe = 0
while True:
    userin = input()
    # print(userin)
    if userin.lower() == 'done':
        break
    arr = intake(userin)
    if check_safe(arr):
        safe += 1
    # print(increase(arr))
    # print(decrease(arr))

print(safe)

