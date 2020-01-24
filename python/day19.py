import sys
import re

# Parsed input placeholders
molecule = None
replacements = []

#
# Iterate the stdin and create the required data structures (replacements list, molecule)
#
for line in sys.stdin:
    line = line.rstrip(' \r\n')

    # Only process non-empty lines
    if len(line) == 0:
        continue
    
    # Try to split into key/value pairs
    components = [component.strip() for component in line.split("=>")]

    # The row was either a replacement key/value pair, or the molecule to replace on
    if len(components) == 1:
        molecule = components[0]
    else:
        replacements.append((components[0], components[1]))

# Keep track of which molecules we have already seen in a set
molecules_after_replacement = set()

# Iterate each possible replacement rule. For each rule, apply it in each position possible
# and keep track of all resulting molecules.
for (key,replacement) in replacements:
    for match in re.finditer(key, molecule):
        new_molecule = ''.join((molecule[:match.span()[0]],replacement,molecule[match.span()[1]:]))
        molecules_after_replacement.add(new_molecule)

# Now the molecules_after_replacement contains all unique resulting molecules from one replacement
print("Part 1: doing one replacement can result in {} different new molecules".format(len(molecules_after_replacement)))

#
# Part 2: 
# We reverse the order and map replacements => keys, sort the entries by length of the replacement,
# then iterate the string from left-to-right for each replacement and reverse it. Repeat until we 
# arrive at only 'e'
#

# Create a vector with the reverse lookup rules
reversed = []
for (key, replacement) in replacements:
    reversed.append((replacement, key))

# Sort it by length of the key
reversed.sort(key = lambda entry: -len(entry[0]))

# Keep track of the state and count each time we do a replacement
tmp = molecule
count = 0

# Replace in the reverse direction, starting with the longest matches
# in case there are substrings which match (these would require more steps)
while not tmp == 'e':
    for r in reversed:
        if r[0] in tmp:
            tmp = tmp.replace(r[0], r[1], 1)
            count += 1
            # print(tmp)

print("Part 2: you can get from 'e' to '{}' in {} steps".format(molecule, count))