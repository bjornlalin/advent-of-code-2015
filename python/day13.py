import sys
import itertools
import numpy as np

def solve(lines, include_yourself=False):

    # Build distance list from input
    id = 0
    ids = {}
    entries = []

    # Read input and build data structures
    for line in lines:

        # Split input
        args = line.replace('.', '').strip('\n').split(' ')

        # extract relevant information
        a = args[0]
        b = args[10]
        sign = args[2]
        value = int(args[3])

        # reverse sign if 'lose' instead of gain
        if sign == 'lose':
            value = -1 * value

        # create lookup table for each location
        if a not in ids:
            ids[a] = id
            id += 1
        if b not in ids:
            ids[b] = id
            id += 1

        # Store tuples (a, b, gain/loss value) in a list
        entries.append((ids[a], ids[b], value))

    # Seat yourself if requested
    if include_yourself:
        ids['me'] = id
        id += 1

    # Create a matrix with the right size and fill it with the scores
    value_matrix = np.zeros([id, id], dtype=int)
    for (a, b, value) in entries:
        value_matrix[a,b] = value

    # Generate all possible seatings (permutations) and calculate the score
    # remember to add scores in both "directions"
    best_score = 0
    for perm in itertools.permutations(ids.values()):
        score = 0
        for i in range(0, len(ids)-1):
            score += value_matrix[perm[i], perm[i+1]]
            score += value_matrix[perm[i+1], perm[i]]

        score += value_matrix[perm[len(ids)-1], perm[0]]
        score += value_matrix[perm[0], perm[len(ids)-1]]

        if score > best_score:
            best_score = score

    return best_score

lines = []
for line in sys.stdin:
    lines.append(line)

print("Part 1: {}".format(solve(lines)))
print("Part 2: {}".format(solve(lines, include_yourself=True)))
