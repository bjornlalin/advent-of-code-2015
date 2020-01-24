import sys

def solve(line):
    # Strip any whitespace / EOL, split by 'x' and convert to integers
    d = list(map(int, line.strip().split("x")))
    # Calculate dimension of paper as specified
    return 2*d[0]*d[1] + 2*d[0]*d[2] + 2*d[1]*d[2] + min(d[0]*d[1], d[0]*d[2], d[1]*d[2])

def solve2(line):
    # Strip any whitespace / EOL, split by 'x' and convert to integers
    d = list(map(int, line.strip().split("x")))

    bow = d[0]*d[1]*d[2]

    d.sort()
    
    return 2*d[0] + 2*d[1] + bow

total1 = 0
total2 = 0
for line in sys.stdin:
    total1 += solve(line)
    total2 += solve2(line)

print('Part 1: {}'.format(total1))
print('Part 2: {}'.format(total2))
