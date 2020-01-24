
import numpy as nd
import math

def lowestHouseNumber(goal):
    lowest = goal
    MAX = int(goal / 10) 
    houses = nd.zeros(MAX+1,dtype=int)

    for elf in range(1, MAX+1):
        for house in range(elf, MAX+1, elf):

            # Deliver gifts
            houses[house] += (elf * 10)

            # Check if we found a house which meets the criteria
            if houses[house] >= goal and house < lowest:
                lowest = house
            
            # debug output
            # print('elf {} delivers {} presents to house {}, which now has {} presents'.format(elf, num_presents, house, houses[house]))

    return lowest                

def lowestHouseNumber2(goal):
    lowest = goal
    MAX = int(goal / 11) 
    houses = nd.zeros(MAX+1,dtype=int)

    for elf in range(1, MAX+1):
        n_visited = 0
        for house in range(elf, MAX+1, elf):

            # Deliver gifts
            houses[house] += (elf * 11)

            # Check if we found a house which meets the criteria
            if houses[house] >= goal and house < lowest:
                lowest = house

            # debug output
            # print('elf {} delivered {} presents to house {}, which now has {} presents'.format(elf, elf*11, house, houses[house]))

            # Max 50 visits per elf
            n_visited += 1
            if n_visited == 50:
                break

    return lowest                

goal = 29000000

print("Part 1: House {} received at least {} presents".format(lowestHouseNumber(goal), goal))
print("Part 2: House {} received at least {} presents".format(lowestHouseNumber2(goal), goal))
