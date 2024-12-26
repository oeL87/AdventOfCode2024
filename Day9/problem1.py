
def create_disk_map(string):
    ret = []
    isFile = True
    fileCount = 0
    for n in string:
        n = int(n)
        if isFile:
            for i in range(n):
                ret.append(str(fileCount))
            fileCount += 1
        else:
            for i in range(n):
                ret.append('.')
        isFile = not isFile
    
    return ret
        
def compact(blocks):
    end = len(blocks)-1
    for n in range(len(blocks)):
        if blocks[n] == '.':
            while blocks[end] == '.':
                end -= 1
            if n >= end:
                break
            temp = blocks[n]
            blocks[n] = blocks[end]
            blocks[end] = temp
            end -= 1
        
def checksum(blocks):
    sum = 0
    for pos in range(len(blocks)):
        if blocks[pos] == '.':
            continue
        val = int(blocks[pos])
        sum += val * pos      
    return sum  

with open("input.txt", "r") as f:
    string = f.read()
    blocks = create_disk_map(string)
    print(blocks[-1:-100:-1])
    compact(blocks)
    print(blocks[-1:-100:-1])
    print(checksum(blocks))
# userin = input("input\n")
# while userin != 'done':
#     string += userin
#     userin = input()
    
# print(string)


