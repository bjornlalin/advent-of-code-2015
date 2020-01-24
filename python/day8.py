import sys
import re

def numCharsInCode(line):
    return len(line)

def numCharsInMemory(line):

    skip = 0
    total = 0

    for c in line[1:-1]:
        if skip > 0:
            skip -= 1
            if c == "x":
                skip = 2
        else:
            total += 1
            if c == "\\":
                skip = 1
    
    return total

def encode(line):
    encoded = "\""
    for c in line:
        if c == "\\":
            encoded += "\\\\"
        elif c == "\"":
            encoded += "\\\""
        else:
            encoded += c
    encoded += "\""

    return encoded

totalInCode = 0
totalInMemory = 0
totalEncoded = 0

for line in sys.stdin:
    totalInCode += numCharsInCode(line.strip())
    totalInMemory += numCharsInMemory(line.strip())
    totalEncoded += len(encode(line.strip()))

print("Part 1: ", totalInCode - totalInMemory)
print("Part 2: ", totalEncoded - totalInCode)

# Debug output
# print("total in code: " , totalInCode)
# print("total in memory: ", totalInMemory)
# print("total encoded: ", totalEncoded)