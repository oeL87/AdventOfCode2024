
def find_xmas(grid):
    word = 'XMAS'
    word_len = 4
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (0,1),
        (1,0),
        (1,1),
        (-1,1),
    ]
    reversed_word = word[::-1]
    count = 0
    
    def is_valid(x,y):
        return 0 <= x < rows and 0 <= y < cols
    
    def search(x,y,dx,dy,target):
        for i in range(len(target)):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != target[i]:
                return False
        return True
    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search(i, j, dx, dy, word) or search(i, j, dx, dy, reversed_word):
                    count += 1

    return count

grid = []
userin = input("input:\n")

while userin != 'done':
    grid.append(list(userin.upper()))
    userin = input()
    
count = find_xmas(grid)
print(count)