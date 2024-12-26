"""
- If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
- If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved 
on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
- If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 
2024 is engraved on the new stone.
"""
def getDigits(val):
    digitCount = 0
    while val > 0:
        val //= 10
        digitCount += 1
    return digitCount

def blink(stones):
    new_stones = []
    for stone in stones:
        digitCount = getDigits(stone)
        if stone == 0:
            new_stones.append(1)
            # print("replaced with 1")
        elif digitCount % 2 == 0:
            first_half = stone//(10**(digitCount/2))
            second_half = stone - first_half*(10**(digitCount/2))
            new_stones.append(int(first_half))
            new_stones.append(int(second_half))
            # print(f"even digit count: {10**(digitCount/2)}   {first_half} {second_half}")
        else:
            new_stones.append(stone*2024)
            # print(f'no other rules')
    return new_stones

with open("./day11/in.txt", "r") as f:
    userin = f.read()
    int_arr = [int(x.strip()) for x in userin.split(' ')]
    print(int_arr)
    blinkCount = 0
    # print(blink([int_arr[0]]))
    while blinkCount < 25:
        int_arr = blink(int_arr)
        # print(f'blink #{blinkCount+1}\n{int_arr}')
        blinkCount += 1
    print(len(int_arr))