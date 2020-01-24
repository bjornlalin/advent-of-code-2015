import sys
import re
from collections import defaultdict

# Compile once only
pattern1 = re.compile(r"a|e|i|o|u") # vowels
pattern2 = re.compile(r'(\w)(\1{1,})') # Repeated characters
pattern3 = re.compile(r"ab|cd|pq|xy") # not one of these

def solve(line):
    string = line.strip()

    # Criteria 1 and 3 we find by Regex
    criteria1 = len(pattern1.findall(string)) >= 3
    criteria2 = len(pattern2.findall(string)) >= 1
    criteria3 = len(pattern3.findall(string)) >= 1

    if criteria1 and criteria2 and not(criteria3):
        return 1 #'nice'

    return  0 #'naughty'

def solve2(line):
    string = line.strip()

    criteria1 = False
    criteria2 = False

    # Criteria 1
    pairs = defaultdict(int)
    lastPair = ''
    for i in range(1, len(string)):
        pair = string[i-1:i+1]

        # Handle special overlapping case
        if pair[0] == pair[1] and pair == lastPair:
            lastPair = ''
        else:
            pairs[pair] += 1
            lastPair = pair

    # Now check if we have any pair which occurs at least twice
    criteria1 = max(pairs.values()) > 1

    # Criteria 2
    for i in range(2, len(string)):
        if string[i-2] == string[i]:
            criteria2 = True
            break

    if criteria1 and criteria2:
        return 1 #'nice'

    return  0 #'naughty'

total1 = 0 
total2 = 0
for line in sys.stdin:
    total1 += solve(line)
    total2 += solve2(line)
    
print("Part 1: {}".format(total1))
print("Part 2: {}".format(total2))