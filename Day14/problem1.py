def print_grid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            # print(f'{x=}', end='')
            if grid[x][y] == 0:
                print('.', end='')
            else:
                print(grid[x][y],end='')
        print()
            


def parse_robot_stats(text):
    groups = text.strip().split('\n')
    robots = []
    for group in groups:
        # print(group)
        robot = {}
        for line in group.split(' '):
            label, coords = line.split('=')
            x_val, y_val = coords.split(',')
            x_val = int(x_val)
            y_val = int(y_val)
            if label == 'p':
                robot['pos'] = {'x': x_val, 'y': y_val}
            elif label == 'v':
                robot['vel'] = {'dx': x_val, 'dy': y_val}
        robots.append(robot)
    return robots

def place_robots(robots):
    grid = [[0 for x in range(101)] for y in range(103)]
    for robot in robots:
        grid[robot.get('pos').get('y')][robot.get('pos').get('x')] += 1
    return grid

def move_robots(robots):
    grid = [[0 for x in range(101)] for y in range(103)]
    for robot in robots:
        x_i = robot.get('pos').get('x')
        dx = robot.get('vel').get('dx')
        x_f = x_i + dx*100        
        y_i = robot.get('pos').get('y')
        dy = robot.get('vel').get('dy')
        y_f = y_i + dy*100
        grid[y_f%103][x_f%101] += 1
    return grid

def calc(grid):
    x = len(grid[0])//2
    y = len(grid)//2
    print(x)
    print(y)
    quadrants = []
    
    for a in range(2):
        for b in range(2):
            total = 0
            for i in range(a*x + a, a*x + x + a):
                for j in range(b*y + b, b*y + y + b):
                    # print(f'({i},{j})')
                    total += grid[j][i]
            quadrants.append(total)
    return quadrants
            
            

with open("./day14/in.txt", "r") as f:
    userin = f.read()
    robots = parse_robot_stats(userin)
    # print(robots)
    # grid = place_robots(robots)
    # print(f'{len(grid)} {len(grid[0])}')
    # print_grid(grid)
    print()
    grid = move_robots(robots)
    # print_grid(grid)
    quadrants = calc(grid)
    total = 1
    for quad in quadrants:
        total *= quad
    print(total)