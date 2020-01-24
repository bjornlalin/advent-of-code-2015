class Item:
    name = None
    damage = None
    armor = None
    def __init__(self, name, price, damage, armor):
        self.name = name
        self.price = price
        self.damage = damage
        self.armor = armor

class Weapon(Item):
    def __init__(self, name, price, damage, armor):
        Item.__init__(self, name, price, damage, armor)

class Armor(Item):
    def __init__(self, name, price, damage, armor):
        Item.__init__(self, name, price, damage, armor)

class Ring(Item):
    def __init__(self, name, price, damage, armor):
        Item.__init__(self, name, price, damage, armor)

class Player:

    name = None
    hitpoints = 0
    _ring1 = None
    _ring2 = None
    _armor = None
    _weapon = None

    def __init__(self, name, hitpoints, weapon, armor, ring1, ring2):
        self.name = name
        self.hitpoints = hitpoints
        self._weapon = weapon
        self._armor = armor
        self._ring1 = ring1
        self._ring2 = ring2

    def armor(self):
        return self._ring1.armor + self._ring2.armor + self._weapon.armor + self._armor.armor

    def damage(self):
        return self._ring1.damage + self._ring2.damage + self._weapon.damage + self._armor.damage

    def price(self):
        return self._ring1.price + self._ring2.price + self._weapon.price + self._armor.price

    def receive_blow_from(self, from_player):
        damage_inflicted = max(1, (from_player.damage() - self.armor()))
        print("Player {} inflicted {} damage on {} who now has {} hit points left".format(from_player.name, damage_inflicted, self.name, self.hitpoints))
        self.hitpoints -= damage_inflicted

    # Fight a player
    def fight(self, other_player):
        print("")
        print("Starting fight between {} and {}".format(self.name, other_player.name))
        print("{} uses weapon: {}, armor: {}, ring 1: {}, ring 2: {}".format(self.name, self._weapon.name, self._armor.name, self._ring1.name, self._ring2.name))
        print("******************************")

        while True:
            other_player.receive_blow_from(self)
            if other_player.hitpoints <= 0:
                return True
            self.receive_blow_from(other_player)
            if self.hitpoints <= 0:
                return False

class Boss(Player):

    def __init__(self):
        self.name = "Boss"
        self.hitpoints = 109
        self._weapon = Weapon("Boss hands", 0, 8, 0)
        self._armor = Armor("Boss skin", 0, 2, 0)
        self._ring1 = Ring("Boss no ring 1", 0, 0, 0)
        self._ring2 = Ring("Boss no ring 2", 0, 0, 0)

# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0
weapons = {
    Weapon("Dagger", 8, 4, 0),
    Weapon("Shortsword", 10, 5, 0),
    Weapon("Warhammer", 25, 6, 0),
    Weapon("Longsword", 40, 7, 0),
    Weapon("Greataxe", 74, 8, 0)
}

# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5
armors = {
    Armor("Leather", 13, 0, 1),
    Armor("Chainmail", 31, 0, 2),
    Armor("Splintmail", 55, 0, 3),
    Armor("Bandedmail", 75, 0, 4),
    Armor("Platemail", 102, 0, 5),
    Armor("No armor", 0, 0, 0)
}

# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3
rings = {
    Ring("Damage +1", 25, 1, 0),
    Ring("Damage +2", 50, 2, 0),
    Ring("Damage +3", 100, 3, 0),
    Ring("Defense +1", 20, 0, 1),
    Ring("Defense +2", 40, 0, 2),
    Ring("Defense +3", 80, 0, 3),
    Ring("No Ring 1", 0, 0, 0),
    Ring("No Ring 2", 0, 0, 0),
}

lowest_price_won = 10000
highest_price_lost = 0

for weapon in weapons:
    for armor in armors:
        for ring1 in rings:
            for ring2 in [ring for ring in rings if ring not in {ring1}]:
                player = Player("Hero", 100, weapon, armor, ring1, ring2)
                boss = Boss()
                
                if player.fight(boss):
                    print("Player won")
                    if player.price() < lowest_price_won:
                        lowest_price_won = player.price()
                else:
                    print("Player lost")
                    if player.price() > highest_price_lost:
                        highest_price_lost = player.price()

print("Part 1: Lowest price to win is {}".format(lowest_price_won))
print("Part 2: Highest price and still losing is {}".format(highest_price_lost))