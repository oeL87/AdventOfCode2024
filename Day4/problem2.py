def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def matches(x,y):
        if x+2 >= rows or y+2 >= cols:
            return False
        sub_grid = [
            [grid[x][y], grid[x][y+1], grid[x][y+2]],
            [grid[x+1][y], grid[x+1][y+1], grid[x+1][y+2]],
            [grid[x+2][y], grid[x+2][y+1], grid[x+2][y+2]],
        ]
        pattern1 = [
            ['M','*','M'],
            ['*','A','*'],
            ['S','*','S'],
        ]
        pattern2 = [
            ['S','*','S'],
            ['*','A','*'],
            ['M','*','M'],
        ]
        pattern3 = [
            ['M','*','S'],
            ['*','A','*'],
            ['M','*','S'],
        ]
        pattern4 = [
            ['S','*','M'],
            ['*','A','*'],
            ['S','*','M'],
        ]
        def match_pattern(grid, pattern):
            for i in range(3):
                for j in range(3):
                    if pattern[i][j] != '*' and grid[i][j] != pattern[i][j]:
                        return False
            return True
        
        return match_pattern(sub_grid, pattern1) or match_pattern(sub_grid, pattern2) or match_pattern(sub_grid, pattern3) or match_pattern(sub_grid, pattern4)
    
    for x in range(rows - 2):
        for y in range(cols - 2):
            if matches(x,y):
                count += 1
                
    return count

grid = []
userin = input("input:\n")

while userin != 'done':
    grid.append(list(userin.upper()))
    userin = input()
    
count = find_xmas(grid)
print(count)