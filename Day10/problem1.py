def findNextTrailheads(top_map):
    heads = set()
    for i in range(len(top_map)):
        for j in range(len(top_map[0])):
            if top_map[i][j] == 0:
                heads.add((i,j))
    return heads
            
def getScore(current, top_map, height=0, visited=None, trail_tips=None):
    if visited is None:
        visited = []
    # if trail_tips is None:
    #     trail_tips = set()
    (x,y) = current
    # print(f'Visiting ({x},{y}) = {top_map[x][y]}, looking for {height}')
    # print(f'({x} {y}) ={top_map[x][y]} {height=}')
    
    if height == 9 and top_map[x][y] == 9 and current not in trail_tips:
        # print(f'Found valid path: {path}')
        print(f"found route {visited}")
        print(f"tips so far {trail_tips}\n ({x,y}) = {top_map[x][y]}")
        trail_tips.add((x,y))
        return 1
    if height == 9:
        return 0
    if top_map[x][y] != height:
        # print(f"invalid node ({x},{y}) != {height}")
        return 0
    visited.append((x,y))
    score = 0
    
    directions = [
        (x-1, y), (x+1, y), (x, y-1), (x, y+1)  
    ]
    
    for next_x, next_y in directions:
        # Check bounds and if not visited
        if (0 <= next_x < len(top_map) and 
            0 <= next_y < len(top_map[0]) and 
            (next_x, next_y) not in visited):
            score += getScore((next_x, next_y), top_map, height + 1, visited, trail_tips=trail_tips)
    # print(f'{trail_tips=}')
    return score
        
def calc(top_map):
    heads = findNextTrailheads(top_map)
    score = 0
    
    # print(next)
    for head in heads:
        trail_tips = set()
        score += getScore(head, top_map,trail_tips=trail_tips)
        print(score)
        # next = findNextTrailhead(top_map, next)
        # print(next)
    # print(f'{heads =}')
    return score

top_map = []
with open("./day10/input.txt", "r") as f:
    for line in f:
        row = [int(num) for num in line.strip()]
        # nums = [int(digit) for digit in string]
        # nums = list(map(int, nums))
        # print(row)
        top_map.append(row)

# heads = findNextTrailheads(top_map)
# print(heads)

score = calc(top_map)

print(f'{score=}')
