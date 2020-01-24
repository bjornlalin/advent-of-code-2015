import sys
import re
import numpy as np

# The readings from the machine
values = {
    "children" : 3,
    "cats" : 7,
    "samoyeds" : 2,
    "pomeranians" : 3,
    "akitas": 0,
    "vizslas" : 0,
    "goldfish" : 5,
    "trees" : 3,
    "cars" : 2,
    "perfumes" : 1
}

# Logic to compare values to the readings from the machine
def process(line, compare):

    id = line.split(' ')[1][0:-1]

    aunt_values = ''.join(line.split(' ')[2:]).strip('\n').split(',')

    for aunt_value in aunt_values:
        trace = aunt_value.split(':')[0]
        value = int(aunt_value.split(':')[1])

        # No match, this particular reading does not match the trace from
        # the parcel so it cannot be this aunt...
        if not compare(trace, value):
            return False

    # If all readings match, we conclude that this is the correct aunt
    print('Sue {} is the correct aunt'.format(id))

# Part 1 comparator
def compare1(trace, value):
    return values[trace] == value

# Part 2 comparator
def compare2(trace, value):
    if trace in ['cats', 'trees']:
        return values[trace] < value
    elif trace in ['pomeranians', 'goldfish']:
        return values[trace] > value
    else:
        return values[trace] == value

for line in sys.stdin:
    process(line, compare1)
    process(line, compare2)
