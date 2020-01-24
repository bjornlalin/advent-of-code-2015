
#
# Check out this:
# https://towardsdatascience.com/solving-travelling-salesperson-problems-with-python-5de7e883d847
#

import sys
import itertools
import numpy as np

# Build distance list from input
id = 0
ids = {}
entries = []

for line in sys.stdin:

    # Parse input line
    args = line.strip().split(' ')
    a = args[0]
    b = args[2]
    dist = int(args[4])

    # create lookup table for each location
    if a not in ids:
        ids[a] = id
        id += 1
    if b not in ids:
        ids[b] = id
        id += 1

    # Store tuples in a list
    entries.append((ids[a], ids[b], dist))

# Create a matrix with the right size
dist_matrix = np.zeros([id, id], dtype=int)

# Fill it with the distance values
for (a, b, dist) in entries:
    dist_matrix[a,b] = dist
    dist_matrix[b,a] = dist

# And finally, calculate the shortest route through brute-force iterating all permutations
shortest = 999999
longest = 0
for perm in itertools.permutations(ids.values()):
    sum = 0
    for i in range(0, len(ids) - 1):
        sum += dist_matrix[perm[i], perm[i+1]]
    if sum < shortest:
        shortest = sum
    if sum > longest:
        longest = sum

print("Part 1 (shortest route): {}".format(shortest))
print("Part 2 (longest route): {}".format(longest))
