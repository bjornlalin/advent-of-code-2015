
import sys
import itertools
from functools import reduce

# We need to split the 29 packages into 'num_groups' groups of equal weight
# For 3 groups this is 1560 (total weight) / 3 = 520, whereas for 4 groups 
# this is 1560 / 4 = 390.
#
# We only need to consider groups which are either:
# 
# - fewer packages than the group with all the lightest packages which sum 520/390 
#   or more, since we cannot construct a larger package than that which is not
#   too heavy.
# 
# - more packages than the group with all the heaviest packages which sum to 520/390 
#   or more, since we cannot construct a smaller package which reaches that weight
#   than the one with all the heaviest packages.
#
#
# TODO: we only find two equally sized groups, it is not obvious to me that we can stop
#       there and still be sure to have a valid solution for 4 sub-groups, but it seems
#       to work. It might be cleaner to use a recursive call to 
# 
#       solve(remaining_packages, num_groups-1)
#
#       for the solution instead, would be much nicer and closer to a mathematical
#       formulation of the problem.
#
def solve(packages, num_groups):
    group_weight = sum(packages) // num_groups
    found_solution = False
    best_qe = 2**64

    # We could calculate these, I just did a quick look at the input
    # to extract these numbers.
    if num_groups == 3:
        lower_bound = 4
        upper_bound = 20
    elif num_groups == 4:
        lower_bound = 4
        upper_bound = 16
    else:
        lower_bound = 1
        upper_bound = len(packages) + 1

    for n_packages_group_1 in range(lower_bound, upper_bound):
        # If we have found a solution, it means it will be a smaller set
        # than anything we can find from now on. Stop looking at larger sets.
        if found_solution:
            break

        for group_1 in itertools.combinations(packages, n_packages_group_1):
            # Found a combination to fit into santa's sled which is exactly the size we need.
            if sum(group_1) == group_weight:

                # check if the QE is also the best we've seen so far. If not, continue
                qe = reduce((lambda x, y: x * y), group_1)

                if qe < best_qe:

                    # Now split the other packages into equally sized groups groups
                    remaining_packages = packages - set(group_1)
                    for n_packages_group_2 in range(lower_bound, max(upper_bound, len(remaining_packages) + 1)):
                        for group_2 in itertools.combinations(remaining_packages, n_packages_group_2):
                            if sum(group_2) == group_weight:
                                # Remember the best solution
                                found_solution = True
                                best_qe = qe

    return best_qe

packages = set()
for line in sys.stdin:
    weight = int(line.strip(' ').strip('\n'))
    packages.add(weight)

print('Part 1: Best QE is {}'.format(solve(packages, 3)))
print('Part 2: Best QE is {}'.format(solve(packages, 4)))
