import numpy as np

def process():
    col1 = []
    col2 = []
    
    while True:
        userin = input()
        if userin.lower() == 'done':
            break
        try:
            num1, num2 = map(float, userin.split())
            col1.append(num1)
            col2.append(num2)
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")
            
    arr1 = np.array(col1)
    arr2 = np.array(col2)
    
    arr1sort = np.sort(arr1)
    arr2sort = np.sort(arr2)
    
    return arr1sort, arr2sort

def make_freq_map(arr):
    freq = {}
    for n in arr:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
            
    return freq
    



arr1, arr2 = process()

# print(arr2)

freq = make_freq_map(arr2)

sum = 0
for n in arr1:
    try:
        sum += n*freq[n]
    except KeyError as e:
        sum += 0
print(sum)