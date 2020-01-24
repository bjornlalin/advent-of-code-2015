
def generate(input, nApply):

    if len(input) == 0:
        return ""

    # Our result string
    result = ""

    # The state 
    count = 1
    last = input[0]

    # The loop
    for c in input[1:]:
        if c != last:
            result += str(count)
            result += last
            count = 0

        last = c
        count += 1

    # The final character
    result += str(count)
    result += last

    # The recursive condition / step
    if nApply > 1:
        return generate(result, nApply-1)
    else:
        return result

# Apply the algorithm to the input 40 times and print the length of the resulting string
print("Part 1: applying the algorithm 40 times results in {} characters".format(len(generate("1113122113", 40))))
print("Part 2: applying the algorithm 50 times results in {} characters".format(len(generate("1113122113", 50))))

