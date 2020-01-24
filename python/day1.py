import sys

def step(char):
    if char == '(':
        return  1
    elif char == ')':
        return - 1
    else:
        raise Exception('Invalid input')


def solve(line):
    floor = 0
    for char in line:
        floor += step(char)

    return floor

def solve2(line):
    pos = 1
    floor = 0
    for char in line:
        floor += step(char)
        if(floor < 0):
            return pos

        pos += 1

    return pos

# Runner
for line in sys.stdin:
    print('Part 1: {}'.format(solve(line)))
    print('Part 2: {}'.format(solve2(line)))

