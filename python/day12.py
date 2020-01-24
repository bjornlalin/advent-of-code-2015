# Note on Python verson: assumes 3.x due to type comparisons

import sys
import re
import json

pattern = re.compile(r"[-]{0,1}\d+")

def solve(line):
    numbers = [int(i) for i in pattern.findall(line)]
    return sum(numbers)

def sum(obj):

    _red = False
    _sum = 0

    if type(obj) is dict:
        for k,v in obj.items():
            if v == 'red':
                _red = True
            else:
                _sum += sum(v)
    elif type(obj) is list:
        for child in obj:
            _sum += sum(child)
    elif type(obj) is not str:
        _sum = obj

    if _red:
        return 0
    
    return _sum

def solve2(line):
    return sum(json.loads(line))

# Solve part 1 and 2
for line in sys.stdin:
    print("Part 1: {}".format(solve(line)))
    print("Part 2: {}".format(solve2(line)))
