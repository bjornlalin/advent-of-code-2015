def solve(row, col):
    mul = 252533
    div = 33554393

    first = 20151125
    for i in range(1, row+col+1):
        for j in range(0, i):
            r, c = i-j, j+1
            # print('[{},{}] = {}'.format(r, c, first))
            if r == row and c == col:
                return first

            first = (first * mul) % div

row, col = 3010, 3019

print(solve(row, col))
