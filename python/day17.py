import sys
import re
import numpy as np

# Read the data into an array
containers = []
for line in sys.stdin:
    containers.append(int(line.strip('\n')))

# solve the problem...

num_solutions = 0
num_solutions_by_num_containers_used = [0] * 20

# Iterate over all combinations of 0's and 1's with 20 values in them (we use bit filters)
for filter in range(0, 2**20):
    liters = 0
    num_containers_used = 0
    # check if each bit is set, and if so, fill the corresponding container with eggnog
    for i in range(0,20):
        if not (0x1 << i) & filter == 0:
            num_containers_used += 1
            liters += containers[i]

    if liters == 150:
        num_solutions += 1
        num_solutions_by_num_containers_used[num_containers_used] += 1

print("Part 1: {}".format(num_solutions))
print("Part 2: {}".format(num_solutions_by_num_containers_used))
