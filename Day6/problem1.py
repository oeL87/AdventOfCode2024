
def navigate_maze(maze):
    # Convert single array of strings to 2D array if needed
    if isinstance(maze[0], str):
        maze = [list(row) for row in maze]
    
    # Directions: right, down, left, up (clockwise)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Find starting position and direction
    start = None
    start_dir = None
    
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell in ['^', '<', '>', 'v']:
                start = (r, c)
                # Map starting character to initial direction index
                start_dir = {'^': 3, 'v': 1, '<': 2, '>': 0}[cell]
                break
        if start:
            break
    
    if start is None:
        return 0  # No starting point found
    
    # Track visited locations and current state
    visited = set([start])
    curr_pos = start
    curr_dir = start_dir
    
    while True:
        # Current direction
        dr, dc = directions[curr_dir]
        new_pos = (curr_pos[0] + dr, curr_pos[1] + dc)
        
        # Check if out of bounds (exit condition)
        if (new_pos[0] < 0 or new_pos[0] >= len(maze) or 
            new_pos[1] < 0 or new_pos[1] >= len(maze[0])):
            break
        
        # Check if hit a block
        if maze[new_pos[0]][new_pos[1]] == '#':
            # Turn right
            curr_dir = (curr_dir + 1) % 4
            continue
        
        # Move and record new position
        curr_pos = new_pos
        visited.add(curr_pos)
    
    return len(visited)

floor = []

userin = input("input:\n")
while userin != 'done':
    floor.append(userin)
    userin = input()
    
output = navigate_maze(floor)
print(output)
    