import sys
import re

#
# Individual Reindeer and logic to calculate distance over time
#
class Reindeer:

    name = None
    flightSpeed = 0
    flightDuration = 0
    restDuration = 0

    # Constructor
    def __init__(self, name, flightspeed, flightDuration, restDuration):
        self.name = name
        self.flightSpeed = flightspeed
        self.flightDuration = flightDuration
        self.restDuration = restDuration
    
    def distance(self, after_seconds):
        complete_flights = after_seconds / (self.flightDuration + self.restDuration)
        additional_flight_seconds = min(self.flightDuration, after_seconds % (self.flightDuration + self.restDuration))
        dist = (self.flightSpeed * self.flightDuration) * complete_flights
        dist += self.flightSpeed * additional_flight_seconds

        return dist

    def __str__(self):
        return "{} can fly {} km/s for {} seconds, but then must rest for {} seconds.".format(self.name, self.flightSpeed, self.flightDuration, self.restDuration)


# Parameters and input
duration = 2503
reindeers = []

# Parse input into reindeers collection
# Example: "Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds."
for line in sys.stdin:
    name = line.split()[0]
    args = re.findall(r"\d+", line)
    reindeers.append(Reindeer(name, int(args[0]), int(args[1]), int(args[2])))

#
# Part 1
# ------
winner = None

for reindeer in reindeers:
    if winner == None:
        winner = reindeer
    elif reindeer.distance(duration) > winner.distance(duration):
        winner = reindeer

print("Part 1: {} flew {} km after {} seconds".format(winner.name, winner.distance(duration), duration))

#
# Part 2
# ------

# setup leaderboard to 0 for everyone
points = {}
for reindeer in reindeers:
    points[reindeer.name] = 0

# Iterate starting from second 1 and finishing at the full final second given
for i in range(1, duration + 1):

    # There can be split winners, each gets a point, so this needs to be a collection
    leaders = []
    
    for reindeer in reindeers:
        if len(leaders) == 0:
            leaders.append(reindeer)
        else:
            if reindeer.distance(i) > leaders[0].distance(i):
                leaders = [reindeer]
            elif reindeer.distance(i) == leaders[0].distance(i):
                leaders.append(reindeer)

    for leader in leaders:
        points[leader.name] = points[leader.name] + 1

    # print("after {} seconds, leaders are: {}".format(i, [x.name for x in leaders]))

print("Part 2 leaderboard: {}".format(points))