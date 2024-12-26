def locate_symbols(floor):
    if isinstance(floor[0], str):
        floor = [list(row) for row in floor]
        
    locations = {}
    
    for x in range(len(floor)):
        for y in range(len(floor)):
            if floor[x][y] == '.':
                continue
            if floor[x][y] not in locations:
                locations[floor[x][y]] = []
            locations[floor[x][y]].append((x,y))
    
    return locations

def findAntinodes(floor, sym_locations):
    if isinstance(floor[0], str):
        floor = [list(row) for row in floor]
    
    count = 0
    rows = len(floor)
    cols = len(floor[0])
    
    for symbol, locations in sym_locations.items():
        if len(locations) < 2:
            continue
        for x in range(len(locations)):
            for y in range(x+1, len(locations)):
                (x1, y1) = locations[x]
                (x2, y2) = locations[y]
                
                if x1 == x2 and abs(y1 - y2) > 1:
                    pot_nodes = [
                        (x1, (y1+y2) // 2),
                        (x1, min(y1,y2) - abs(y1-y2) // 2),
                        (x1, max(y1,y2) + abs(y1-y2) // 2)
                    ]
                elif y1 == y2 and abs(x1 - x2) > 1:
                    pot_nodes = [
                        ((x1 + x2) // 2,  y1),
                        (min(x1,x2) - abs(x1-x2) // 2, y1),
                        (max(x1,x2) + abs(x1-x2) // 2, y1)
                    ]
                else:
                    dx = x2 - x1
                    dy = y2 - y1
                    
                    # Only consider if row and column changes are non-zero and the proportionality allows for an antinode
                    if dx != 0 and dy != 0 and abs(dy) != abs(dx):
                        potential_antinodes = []
                        
                        # Check midpoint
                        midpoint_x = (x1 + x2) // 2
                        midpoint_y = (y1 + y2) // 2
                        potential_antinodes.append((midpoint_x, midpoint_y))
                        
                        # Check before and after points
                        # Proportional scaling to find potential antinodes
                        # Scale both row and column directions
                        before_scale = -(abs(dx) // 2)
                        after_scale = abs(dx) // 2
                        
                        # Before point
                        before_x = x1 + before_scale * (1 if dx > 0 else -1)
                        before_y = y1 + before_scale * (dy / abs(dy)) * (1 if dy > 0 else -1)
                        potential_antinodes.append((int(before_x), int(before_y)))
                        
                        # After point
                        after_x = x2 + after_scale * (1 if dx > 0 else -1)
                        after_y = y2 + after_scale * (dy / abs(dy)) * (1 if dy > 0 else -1)
                        potential_antinodes.append((int(after_x), int(after_y)))
                    else:
                        continue
                
                
    floor = [''.join(row) for row in floor]
    floor = '\n'.join(floor)
    print(floor)
    return count





floor = []

userin = input("input:\n")
while userin != 'done':
    floor.append(userin)
    userin = input()
    
symbol_locations = locate_symbols(floor)
print(symbol_locations)
count = findAntinodes(floor, sym_locations=symbol_locations)
print(count)