import sys
from functools import reduce

ingredients = {}
for line in sys.stdin:
    tokens = line.replace('\n','').replace(',','').replace(':','').split(' ')
    ingredients[tokens[0]] = [tokens[i] for i in [2,4,6,8,10]]
    
print(ingredients)

class Cookie:

    def __init__(self, sprinkles, peanutbutter, frosting, sugar):
        self.sprinkles = sprinkles
        self.peanutbutter = peanutbutter
        self.frosting = frosting
        self.sugar = sugar

    def score(self):
        sums = []
        for ingr in range(0, 4):
            sums.append(self.sprinkles * int(ingredients['Sprinkles'][ingr]) 
            + self.peanutbutter * int(ingredients['PeanutButter'][ingr]) 
            + self.frosting * int(ingredients['Frosting'][ingr]) 
            + self.sugar * int(ingredients['Sugar'][ingr]))

        return max(0, sums[0]) * max(0, sums[1]) * max(0, sums[2]) * max(0, sums[3])

    def calories(self):
        return (self.sprinkles * int(ingredients['Sprinkles'][4]) 
        + self.peanutbutter * int(ingredients['PeanutButter'][4]) 
        + self.frosting * int(ingredients['Frosting'][4]) 
        + self.sugar * int(ingredients['Sugar'][4]))

best = 0
best_lowcal = 0
for i in range(0, 100):
    for j in range(0, 100 - i + 1):
        for k in range(0, 100 - i - j + 1):
            l = 100 - i - j - k
            cookie = Cookie(i, j, k, l)
            if cookie.score() > best:
                best = cookie.score()
            if cookie.calories() == 500 and cookie.score() > best_lowcal:
                best_lowcal = cookie.score()


print("Part 1: the highest scoring cookie receives {} points".format(best)) 
print("Part 2: the highest scoring low-calorie cookie receives {} points".format(best_lowcal)) 
