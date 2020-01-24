import sys
import re

wire_formulas = {}
wire_values = {}

# Split all lines into LHS and RHS and store them in a dictionary
def add_wire(line):
    lh = line.split("->")[0].strip().split(" ")
    rh = line.split("->")[1].strip()
    wire_formulas[rh] = lh
    print(rh, lh)

# Evaluate a wire by calculating the formula and caching it, traversing the 
# circuit from the output and back
def eval(wire):

    # integer values, not a wire
    if re.match(r"^\d+$", wire) is not None:
        return int(wire)

    # Calculate and write to cache if not already calculated
    if(not wire in wire_values):
        wire_values[wire] = 0xffff & eval_formula(wire_formulas[wire])

    # Return value from cache
    return wire_values[wire]

# Parse a formula and apply the correct logic   
def eval_formula(wire_formula):

    # single-word command is either a static int value or another wire
    if len(wire_formula) == 1:
        return eval(wire_formula[0])

    # two word command is always a NOT command   
    if len(wire_formula) == 2:
        return eval_not(wire_formula[1])

    # three-word is one of AND, OR, LSHIFT or RSHIFT
    if len(wire_formula) == 3:
        if(wire_formula[1] == "OR"):
            return eval_or(wire_formula[0], wire_formula[2])
        if(wire_formula[1] == "AND"):
            return eval_and(wire_formula[0], wire_formula[2])
        if(wire_formula[1] == "LSHIFT"):
            return eval_lshift(wire_formula[0], int(wire_formula[2]))
        if(wire_formula[1] == "RSHIFT"):
            return eval_rshift(wire_formula[0], int(wire_formula[2]))

def eval_lshift(wire1, shift):
    return eval(wire1) << shift

def eval_rshift(wire1, shift):
    return eval(wire1) >> shift

def eval_and(wire1, wire2):
    return eval(wire1) & eval(wire2)

def eval_or(wire1, wire2):
    return eval(wire1) | eval(wire2)

def eval_not(wire1):
    return ~ eval(wire1)

# construct all wire formulas
for line in sys.stdin:
    add_wire(line)

# Debug output (all wires)
#for wire in wire_formulas:
#    print(wire, ":", eval(wire))

# Final output
print(eval('a'))

# Part 2
# ------
# reset the cache and redo the calculations, 
# giving the value from 'a' as input to 'b'
# (the output for 'a' was 46065)
wire_values = {}
add_wire("46065 -> b")

print(eval('a'))