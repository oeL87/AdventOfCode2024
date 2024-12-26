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


def sum_distance(arr1, arr2):
    sum = 0
    for i, n in enumerate(arr1):
        sum += abs(arr1[i] - arr2[i])
    return sum
        
        
        
arr1, arr2 = process()
sum = sum_distance(arr1, arr2)

print(sum)
