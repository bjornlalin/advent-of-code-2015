import copy

# Constants and lookups
MAGIC_MISSILE = "Magic Missile"
DRAIN = "Drain"
SHIELD = "Shield"
POISON = "Poison"
RECHARGE = "Recharge"

SPELLS_COST = { 
    MAGIC_MISSILE: 53, 
    DRAIN: 73,
    SHIELD: 113,
    POISON: 173,
    RECHARGE: 229
}

class Spell:

    def __init__(self, name, cost, duration):
        self.turns_active = 0
        self.name = name
        self.cost = cost
        self.duration = duration

    def clone(self):
        return copy.deepcopy(self)

    def apply(self, player, boss):
        self.apply_to_player(player)
        self.apply_to_boss(boss)
        
        self.turns_active += 1

        if self.turns_active == self.duration:
            player.remove_spell(self.name)

    def apply_to_player(self, player):
        raise "NotImplemented"

    def apply_to_boss(self, boss):
        raise "NotImplemented"

class MagicMissile (Spell):
    def __init__(self):
        super().__init__(name = MAGIC_MISSILE, cost = 53, duration = 1)

    def apply_to_player(self, player):
        pass

    def apply_to_boss(self, boss):
        boss.hitpoints -= 4

class Drain (Spell):
    def __init__(self):
        super().__init__(name = DRAIN, cost = 73, duration = 1)

    def apply_to_player(self, player):
        player.hitpoints += 2

    def apply_to_boss(self, boss):
        boss.hitpoints -= 2

class Shield (Spell):
    def __init__(self):
        super().__init__(name = SHIELD, cost = 113, duration = 6)

    def apply_to_player(self, player):
        player.armor = 7

    def apply_to_boss(self, boss):
        pass

class Poison (Spell):
    def __init__(self):
        super().__init__(name = POISON, cost = 173, duration = 6)

    def apply_to_player(self, player):
        pass

    def apply_to_boss(self, boss):
        boss.hitpoints -= 3

class Recharge (Spell):
    def __init__(self):
        super().__init__(name = RECHARGE, cost = 229, duration = 5)

    def apply_to_player(self, player):
        player.mana += 101

    def apply_to_boss(self, boss):
        pass

class Player:

    def __init__(self, hitpoints, mana):
        self.name = "Hero"
        self.armor = 0
        self.consumed_mana = 0
        self.active_spells = {}

        self.hitpoints = hitpoints
        self.mana = mana

    def clone(self):
        return copy.deepcopy(self)

    def can_lay_spell(self, spell_name):
        return spell_name not in self.active_spells.keys() and SPELLS_COST[spell_name] <= self.mana

    def lay_spell(self, spell):
        self.armor = 0 # reset armor
        self.mana -= spell.cost # deduce cost of spell from player mana
        self.consumed_mana += spell.cost # keep track of how much mana we spent (without effect of recharge)
        self.active_spells[spell.name] = spell # add spell to list of active spells
        
    def turn(self, boss):
        for spell_name in self.active_spells.copy().keys():
            self.active_spells[spell_name].apply(self, boss)

    def remove_spell(self, spell_name):
        del self.active_spells[spell_name]

    def __str__(self):
        return "{}: hp={},mana={}".format(self.name, self.hitpoints, self.mana)

class Boss:
    def __init__(self, hitpoints, damage):
        self.name = "Boss"
        self.hitpoints = hitpoints
        self.damage = damage
    
    def turn(self, player):
        player.hitpoints -= max(1, self.damage - player.armor)
#       print('Boss hit player and caused {} damage'.format(max(1, self.damage - player.armor)))

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return "{}: hp={}".format(self.name, self.hitpoints)

#
# Exhaustive search algorithm which tries all possible spells from a given starting state and continues 
# doing a DFS until the fight is finished
#

def possible_spells(player):
    possible_spells = set()

    if player.can_lay_spell(MAGIC_MISSILE):
        possible_spells.add(MagicMissile())
    if player.can_lay_spell(DRAIN):
        possible_spells.add(Drain())
    if player.can_lay_spell(SHIELD):
        possible_spells.add(Shield())
    if player.can_lay_spell(POISON):
        possible_spells.add(Poison())
    if player.can_lay_spell(RECHARGE):
        possible_spells.add(Recharge())
 
    return possible_spells

def search(best_seen, history, player, boss, player_damage_per_turn=0):

    # If we have already seen a better solution, no need to continue searching
    if player.consumed_mana > best_seen:
        return best_seen

    # Part 2 condition
    player.hitpoints -= player_damage_per_turn
    if player.hitpoints <= 0:
        return best_seen

    # We cannot cast any spells, not enough mana. Player lost.
    if len(possible_spells(player)) == 0:
        return best_seen

    # Try each possible spell from this state
    for spell in possible_spells(player):

        # Make a clone of the current state of player and boss
        p = player.clone()
        b = boss.clone()

        # Player's move
        p.lay_spell(spell)
        p.turn(b)

        # Check if boss died
        if b.hitpoints <= 0:
            # If boss died, don't continue searching
            if p.consumed_mana < best_seen:
                best_seen = p.consumed_mana
                #print('BOSS DIED: {} => {}'.format(history + [spell.name], best_seen))
        else:
            # Let the boss do it's move
            b.turn(p)

            # If player is still alive, apply any effects of spells again
            if p.hitpoints > 0:
                p.turn(b)
                if b.hitpoints <= 0:
                    if p.consumed_mana < best_seen:
                        best_seen = p.consumed_mana
                        #print('BOSS DIED: {} => {}'.format(history + [spell.name], best_seen))
                else:
                    # Continue down the search tree
                    best_seen = min(best_seen, search(best_seen, history + [spell.name], p, b, player_damage_per_turn))
                
    return best_seen

player = Player(50, 500)
boss = Boss(55, 8)

print("Part 1: smallest amount of consumed mana: {}".format(search(9999, [], player, boss)))
print("Part 2: smallest amount of consumed mana: {}".format(search(9999, [], player, boss, player_damage_per_turn=1)))