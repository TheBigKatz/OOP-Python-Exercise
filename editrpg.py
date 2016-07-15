"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time
# class Character has a dunder-init that takes self parameter.
class Character(object):
    def __init__(self):
        # From self get the name attribute and set it to undefined
        self.name = '<undefined>'
        # From self get the health attribute and set it to 10.
        self.health = 10
        # From self get the power attribute and set it to 5.
        self.power = 5
        # From self get the coins attribute and set it to 20.
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)
# class Hero has a dunder-init that takes the self parameter.
class Hero(Character):
    def __init__(self):
        # From self get the name attribute and set it to hero.
        self.name = 'hero'
        # From self get the health attribute and set it to 10.
        self.health = 10
        # From self get the power attribute and set it to 5.
        self.power = 5
        # From self get the coins attribute and set it to 20.
        self.coins = 20

    def restore(self):
        # From self get th health attribute and set it to 10.
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)
# class Goblin has a dunder-init that takes the self parameter.
class Goblin(Character):
    def __init__(self):
        # From self get the name attribute and set it to goblin.
        self.name = 'goblin'
        # From self get the health attribute and set it to 6.
        self.health = 6
        # From self get the power attribute and set it to 2.
        self.power = 2
# Make a class named Wizard that inherits Character.
class Wizard(Character):
    # class Wizard has a dunder-init that takes the self parameter.
    def __init__(self):
        # From self get the name attribute and set it to wizard.
        self.name = 'wizard'
        # From self get the health attribute and set it to 8.
        self.health = 8
        # From self get the power attribute and set it to 1.
        self.power = 1

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False
# Make a class named Tonic that inherits object.
class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)
# Make a class named Sword that inherits object.
class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, character):
        character.power += 2
        print "%s's power increased to %d." % (character.name, character.power)
# Make a class named Shopping that inherits object.
class Shopping(object):
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Shopping.items)):
                item = Shopping.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Shopping.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)
# Set hero to an instance of class Hero.
hero = Hero()
enemies = [Goblin(), Wizard()]
battle_engine = Battle()
shopping_engine = Shopping()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
