
def get_int_arr(userin):
    int_arr = [int(x.strip()) for x in userin.split(',')]
    return int_arr

def get_rule_pair(userin):
    return list(map(int, userin.split('|')))

def is_valid(int_arr, page_rules):
    index_map = {num: idx for idx, num in enumerate(int_arr)}
    
    for rule in page_rules:
        # print(f'{rule=}')
        # print(f'{index_map[rule[0]]=} {index_map[rule[1]]=}')
        if rule[0] not in index_map or rule[1] not in index_map:
            continue
        if index_map[rule[0]] >= index_map[rule[1]]:
            return False
    
    return True
    


page_rules = []
rule_arr = []

userin = input("input:\n")
while userin != 'done':
    page_rules.append(userin)
    userin = input()
    
# print(page_rules)
for p in page_rules:
    rule_arr.append(get_rule_pair(p))
# print(rule_arr)

total = []
userin = input("input2:\n")
while userin != 'done':
    arr = get_int_arr(userin)
    if (is_valid(arr, rule_arr)):
        print(arr[len(arr)//2])
        total.append(arr[len(arr)//2])
    userin = input()
    
# print(rule_arr)
print(total)
print(sum(total))
