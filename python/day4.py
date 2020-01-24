import sys
import hashlib

def find(line, nZeroes = 5):
    number = 1
    secret = line.strip()
    
    while True:
        input = "{}{}".format(secret, number)
        hash = hashlib.md5(input.encode('utf-8')).hexdigest()
        if(hash[0:nZeroes] == "0" * nZeroes):
            break
        number += 1
    
    return number

def solve(line):
    return find(line)

def solve2(line):
    return find(line, 6)

for line in sys.stdin:
    print('Part 1: {}'.format(solve(line)))
    print('Part 2: {}'.format(solve2(line)))
