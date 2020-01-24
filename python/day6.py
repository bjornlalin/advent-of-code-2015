import sys
import re
import numpy as np

# Create matrix of 0's
square = np.zeros(shape = (1000, 1000), dtype = bool)

# We use this to parse the input
pattern = re.compile(r"([0-9]+\,[0-9]+)")

def process(line):

    coords = pattern.findall(line)
    rowFrom = int(coords[0].split(",")[0])
    rowTo = int(coords[1].split(",")[0]) + 1
    colFrom = int(coords[0].split(",")[1])
    colTo = int(coords[1].split(",")[1]) + 1

    # XOR
    if line.startswith("toggle"):
        square[rowFrom:rowTo, colFrom:colTo] = np.logical_not(square[rowFrom:rowTo, colFrom:colTo])
    
    # Set to True
    if line.startswith("turn on"):
        square[rowFrom:rowTo, colFrom:colTo] = True

    # Set to False
    if line.startswith("turn off"):
        square[rowFrom:rowTo, colFrom:colTo] = False

square2 = np.zeros(shape = (1000, 1000), dtype = int)

def process2(line):

    coords = pattern.findall(line)
    rowFrom = int(coords[0].split(",")[0])
    rowTo = int(coords[1].split(",")[0]) + 1
    colFrom = int(coords[0].split(",")[1])
    colTo = int(coords[1].split(",")[1]) + 1

    # XOR
    if line.startswith("toggle"):
        square2[rowFrom:rowTo, colFrom:colTo] += 2
    
    # Set to True
    if line.startswith("turn on"):
        square2[rowFrom:rowTo, colFrom:colTo] += 1

    # Set to False
    if line.startswith("turn off"):
        square2[rowFrom:rowTo, colFrom:colTo][square2[rowFrom:rowTo, colFrom:colTo] > 0] -= 1

for line in sys.stdin:
    process(line)
    process2(line)

# Finally, print result
print(np.sum(square))
print(np.sum(square2))
