
def parse_coordinate_sets(input_text):
    """
    Parses text input containing button and prize coordinates into a list of dictionaries.
    
    Args:
        input_text (str): String containing multiple sets of coordinates
        
    Returns:
        list: List of dictionaries, each containing coordinates for Button A, Button B, and Prize
    """
    # Split input into groups (each group contains Button A, Button B, and Prize)
    groups = input_text.strip().split('\n\n')
    result = []
    
    for group in groups:
        coordinates = {}
        
        # Process each line in the group
        for line in group.strip().split('\n'):
            # Split into label and coordinates
            label, coords = line.split(': ')
            
            # Extract X and Y values
            x_part, y_part = coords.split(', ')
            
            # Parse X and Y values, handling both relative (+) and absolute (=) values
            x_value = int(x_part[1:].replace('+', '').replace('=', ''))
            y_value = int(y_part[1:].replace('+', '').replace('=', ''))
            
            # Store in dictionary using normalized keys
            if label == 'Button A':
                coordinates['button_a'] = {'x': x_value, 'y': y_value}
            elif label == 'Button B':
                coordinates['button_b'] = {'x': x_value, 'y': y_value}
            elif label == 'Prize':
                coordinates['prize'] = {'x': x_value, 'y': y_value}
        
        result.append(coordinates)
    
    return result

def calc1prize(dictionary):
    but_a = dictionary.get('button_a')
    but_b = dictionary.get('button_b')
    prize = dictionary.get('prize')
    # print(f'{but_a=} {but_b=} {prize=}')
    def tryXAYB(x, y):
        bigX = but_a.get('x') * x + but_b.get('x') * y == prize.get('x')
        bigY = but_a.get('y') * x + but_b.get('y') * y == prize.get('y')
        # print(f'{bigX=} {bigY=}')
        return bigX and bigY
    
    def findMin():
        min = 600
        for i in range(100):
            for j in range(100):
                if tryXAYB(i, j) and i*3 + j < min:
                    min = i*3 + j
        if min == 600:
            return None
        return min
    
    return findMin()
                
def calc(dictionaries):
    total = 0
    for dictionary in dictionaries:
        tokens = calc1prize(dictionary)
        if tokens is None:
            continue
        total += tokens
    return total
        

with open("./day13/in.txt", "r") as f:
    userin = f.read()
    dictionary = parse_coordinate_sets(userin)
    # print(dictionary)
    # print(calc1prize(dictionary[0]))
    print(calc(dictionary))