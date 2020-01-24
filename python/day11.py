
# No 'i', 'l' or 'o' may be used
alphabet = "abcdefghjkmnpqrstuvwxyz" 

# Let's build a reverse lookup array to find the index
# in the alphabet array of a given character.
index = 0
indexes = {}
for c in alphabet:
    indexes[c] = index
    index += 1

# After we have 5 characters, the available options start to drop quite significantly.
#
# How many possibilities are there even? With no restrictions there are 26^8 = 208'827'064'576
# possibilities, so more than 200 billion. That's too much to solve in a brute-force way
# on a simple laptop. On the other hand, just starting from any point, we can expect the required
# iterations to be reasonable, so let's start with a simple brute-force approach.
# 

def generateNew(old):
    new = next(old)
    while not valid(new):
        new = next(new)

    return new

def next(current):
    tmp = list(current)
    pos = 7
    while tmp[pos] == 'z':
        tmp[pos] = 'a'
        pos = pos - 1
    
    tmp[pos] = chr(ord(tmp[pos]) + 1)

    return ''.join(tmp)

def valid(phrase):

    # Banned characters
    for c in phrase:
        if c in ['i','l','o']:
            return False

    # find repeated pairs of characters
    repeated = []

    for i in range(0,7):
        if phrase[i] == phrase[i+1]:
            repeated.append(i)

    # There is only 0 or 1 repeated pairs, or there is an overlap
    if not (len(repeated) > 1 and repeated[len(repeated) - 1] - repeated[0] > 1):
        return False

    # sequences of 3 consecutive and increasing characters. If we find one, all
    # other criteria are also met so we can return true
    for i in range(0,6):
        if ord(phrase[i]) == ord(phrase[i+1])-1 and ord(phrase[i+1]) == ord(phrase[i+2])-1:
            return True

    return False
    
# Some functional tests
test = False

if(test):
    # Validity testing
    print("{}: {}".format("aaabcdef", valid("aaabcdef")))
    print("{}: {}".format("aabbxyzs", valid("aabbxyzs")))
    print("{}: {}".format("aabbxyxy", valid("aabbxyxy")))
    print("{}: {}".format("abcdefff", valid("abcdefff")))
    print("{}: {}".format("aabcddei", valid("aabcddei")))
    print("")
    # Calculation of next pwd
    print("{}: {}".format("aaaaaaaa", next("aaaaaaaa")))
    print("{}: {}".format("aaaaaaay", next("aaaaaaay")))
    print("{}: {}".format("aaaaaaaz", next("aaaaaaaz")))
    print("{}: {}".format("aaaaaafz", next("aaaaaafz")))
    print("{}: {}".format("aaaaaazz", next("aaaaaazz")))
    print("")

print('Part 1: {}'.format(generateNew('cqjxjnds')))
print('Part 2: {}'.format(generateNew(generateNew('cqjxjnds'))))