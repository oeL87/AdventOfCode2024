def can_make(target, numbers):
    def dfs(index, current_value):
        if index == len(numbers):
            return current_value == target
        next = numbers[index]
        if dfs(index+1, current_value + next):
            return True
        if dfs(index+1, current_value*next):
            return True
        return False
    return dfs(1, numbers[0])




userin = input("inputs:\n")
sum = 0

while userin != 'done':
    target_str, rest = userin.split(':', 1)
    target_int = int(target_str.strip())
    arr = list(map(int, rest.strip().split()))
    if can_make(target_int, arr):
        sum += target_int
    userin = input()

print(sum)
# print(target_int)
# print(arr)