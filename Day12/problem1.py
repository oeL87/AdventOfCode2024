def analyze_regions(grid):
    """
    Analyzes a 2D grid of characters to find connected regions and calculate their areas and perimeters.
    
    Args:
        grid: List[List[str]] - 2D array of characters
        
    Returns:
        List[dict] - List of dictionaries containing information about each region:
            - letter: The character that forms the region
            - area: Number of connected cells
            - perimeter: Number of edges exposed to different characters or grid boundaries
    """
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    regions = []
    
    def get_neighbors(r, c):
        """Returns valid neighboring cell coordinates."""
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        return [(r + dr, c + dc) for dr, dc in directions
                if 0 <= r + dr < rows and 0 <= c + dc < cols]
    
    def explore_region(r, c, letter):
        """
        Explores a region using DFS and returns its area and perimeter.
        """
        if (r, c) in visited or grid[r][c] != letter:
            return 0, 0
        
        visited.add((r, c))
        area = 1
        perimeter = 0
        
        for nr, nc in get_neighbors(r, c):
            if grid[nr][nc] == letter:
                new_area, new_perim = explore_region(nr, nc, letter)
                area += new_area
                perimeter += new_perim
            else:
                perimeter += 1
                
        if r == 0: perimeter += 1
        if r == rows - 1: perimeter += 1
        if c == 0: perimeter += 1
        if c == cols - 1: perimeter += 1
        
        return area, perimeter
    
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                area, perimeter = explore_region(r, c, grid[r][c])
                if area > 0:
                    regions.append({
                        'letter': grid[r][c],
                        'area': area,
                        'perimeter': perimeter
                    })
    
    return regions

garden = []
with open("./day12/in.txt", "r") as f:
    for line in f:
        row = [num for num in line.strip()]
        garden.append(row)

regions = analyze_regions(garden)
print(regions)
sum = 0
for region in regions:
    area = region.get('area')
    peri = region.get('perimeter')
    sum += area*peri
    print(area*peri)
print(sum)