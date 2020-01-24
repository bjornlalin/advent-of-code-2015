import sys


def deliver(line, roboSanta = False):

    # initial delivery
    hash = {'0#0': 1}

    coords = [
        [0,0], # x,y Santa
        [0,0]  # x,y Robo-Santa
    ]
    step = 0
    for char in line:
        
        if roboSanta:
            santa = step % 2
        else:
            santa = step % 1

        # move
        if char == '>':
            coords[santa][0] += 1
        if char == '<':
            coords[santa][0] -= 1
        if char == '^':
            coords[santa][1] += 1
        if char == 'v':
            coords[santa][1] -= 1

        # mark delivered location
        hash["{}#{}".format(coords[santa][0],coords[santa][1])] = 1

        step += 1

    return len(hash)

def solve(line):
    return deliver(line, False)

def solve2(line):
    return deliver(line, True)

for line in sys.stdin:
    print('Part 1: {}'.format(solve(line)))
    print('Part 2: {}'.format(solve2(line)))
