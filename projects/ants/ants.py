"""CS 61A presents Ants Vs. SomeBees."""

import random
from ucb import main, interact, trace
from collections import OrderedDict

################
# Core Classes #
################


class Place(object):
    """A Place holds insects and has an exit to another Place."""
    def __init__(self, name, exit=None):
        """Create a Place with the given NAME and EXIT.

        name -- A string; the name of this Place.
        exit -- The Place reached by exiting this Place (may be None).
        """
        self.name = name
        self.exit = exit
        self.bees = []  # A list of Bees
        self.ant = None  # An Ant
        self.entrance = None  # A Place
        # Phase 1: Add an entrance to the exit
        # BEGIN Problem 2
        "*** YOUR CODE HERE ***"
        if exit is not None:
            exit.entrance = self
        # END Problem 2

    def add_insect(self, insect):
        """Add an Insect to this Place.

        There can be at most one Ant in a Place, unless exactly one of them is
        a container ant (Problem 9), in which case there can be two. If add_insect
        tries to add more Ants than is allowed, an assertion error is raised.

        There can be any number of Bees in a Place.
        """
        if insect.is_ant:
            if self.ant is None:
                self.ant = insect
            else:
                # BEGIN Problem 9
                if self.ant.is_container and self.ant.can_contain(insect):
                    self.ant.contain_ant(insect)
                elif insect.is_container and insect.can_contain(self.ant):
                    insect.contain_ant(self.ant)
                    self.ant = insect
                else:
                    assert self.ant is None, 'Two ants in {0}'.format(self)
                # END Problem 9
        else:
            self.bees.append(insect)
        insect.place = self

    def remove_insect(self, insect):
        """Remove an INSECT from this Place.

        A target Ant may either be directly in the Place, or be contained by a
        container Ant at this place. The true QueenAnt may not be removed. If
        remove_insect tries to remove an Ant that is not anywhere in this
        Place, an AssertionError is raised.

        A Bee is just removed from the list of Bees.
        """
        if insect.is_ant:
            # Special handling for QueenAnt
            # BEGIN Problem 13
            "*** YOUR CODE HERE ***"
            if isinstance(insect, QueenAnt) and insect.is_true_queen:
                return
            # END Problem 13

            # Special handling for container ants
            if self.ant is insect:
                # Bodyguard was removed. Contained ant should remain in the game
                if hasattr(self.ant, 'is_container') and self.ant.is_container:
                    self.ant = self.ant.contained_ant
                else:
                    self.ant = None
            else:
                # Contained ant was removed. Bodyguard should remain
                if hasattr(self.ant, 'is_container') and self.ant.is_container \
                        and self.ant.contained_ant is insect:
                    self.ant.contained_ant = None
                else:
                    assert False, '{0} is not in {1}'.format(insect, self)
        else:
            self.bees.remove(insect)

        insect.place = None

    def __str__(self):
        return self.name


class Insect(object):
    """An Insect, the base class of Ant and Bee, has armor and a Place."""

    is_ant = False
    damage = 0
    # ADD CLASS ATTRIBUTES HERE
    is_watersafe = False

    def __init__(self, armor, place=None):
        """Create an Insect with an ARMOR amount and a starting PLACE."""
        self.armor = armor
        self.place = place  # set by Place.add_insect and Place.remove_insect

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the insect from its place if it
        has no armor remaining.

        >>> test_insect = Insect(5)
        >>> test_insect.reduce_armor(2)
        >>> test_insect.armor
        3
        """
        self.armor -= amount
        if self.armor <= 0:
            self.place.remove_insect(self)

    def action(self, colony):
        """The action performed each turn.

        colony -- The AntColony, used to access game state information.
        """

    def __repr__(self):
        cname = type(self).__name__
        return '{0}({1}, {2})'.format(cname, self.armor, self.place)


class Bee(Insect):
    """A Bee moves from place to place, following exits and stinging ants."""

    name = 'Bee'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    is_watersafe = True

    def __init__(self, armor, place=None):
        super().__init__(armor, place)
        self.is_scared = False
        self.scared_once = False

    def sting(self, ant):
        """Attack an ANT, reducing its armor by 1."""
        ant.reduce_armor(self.damage)

    def move_to(self, place):
        """Move from the Bee's current Place to a new PLACE."""
        self.place.remove_insect(self)
        place.add_insect(self)

    def blocked(self):
        """Return True if this Bee cannot advance to the next Place."""
        # Phase 4: Special handling for NinjaAnt
        # BEGIN Problem 7
        return self.place.ant is not None and self.place.ant.blocks_path
        # END Problem 7

    def action(self, colony):
        """A Bee's action stings the Ant that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.

        colony -- The AntColony, used to access game state information.
        """
        destination = self.place.exit
        # Extra credit: Special handling for bee direction
        # BEGIN EC
        "*** YOUR CODE HERE ***"
        if self.is_scared:
            if self.place.entrance is colony.hive:
                destination = self.place
            else:
                destination = self.place.entrance
        # END EC
        if self.blocked():
            self.sting(self.place.ant)
        elif self.armor > 0 and destination is not None:
            self.move_to(destination)


class Ant(Insect):
    """An Ant occupies a place and does work for the colony."""

    is_ant = True
    implemented = False  # Only implemented Ant classes should be instantiated
    food_cost = 0
    # ADD CLASS ATTRIBUTES HERE
    blocks_path = True
    is_container = False

    def __init__(self, armor=1):
        """Create an Ant with an ARMOR quantity."""
        Insect.__init__(self, armor)

    def can_contain(self, other):
        return False


class HarvesterAnt(Ant):
    """HarvesterAnt produces 1 additional food per turn for the colony."""

    name = 'Harvester'
    implemented = True
    # OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 2

    def action(self, colony):
        """Produce 1 additional food for the COLONY.

        colony -- The AntColony, used to access game state information.
        """
        # BEGIN Problem 1
        "*** YOUR CODE HERE ***"
        colony.food += 1
        # END Problem 1


class ThrowerAnt(Ant):
    """ThrowerAnt throws a leaf each turn at the nearest Bee in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 3
    max_range = None
    min_range = None

    def nearest_bee(self, hive):
        """Return the nearest Bee in a Place that is not the HIVE, connected to
        the ThrowerAnt's Place by following entrances.

        This method returns None if there is no such Bee (or none in range).
        """

        # BEGIN Problem 3 and 4
        def find_nearest_bees_start_from(place, distance=0):
            if place is hive:
                return
            if len(place.bees) > 0 and (
                (self.max_range is None and self.min_range is None) or
                (self.max_range is not None and self.max_range >= distance) or
                (self.min_range is not None and self.min_range <= distance)):
                return place.bees
            return find_nearest_bees_start_from(place.entrance, distance + 1)

        return random_or_none(find_nearest_bees_start_from(self.place))
        # END Problem 3 and 4

    def throw_at(self, target):
        """Throw a leaf at the TARGET Bee, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a leaf at the nearest Bee in range."""
        self.throw_at(self.nearest_bee(colony.hive))


def random_or_none(s):
    """Return a random element of sequence S, or return None if S is empty."""
    if s:
        return random.choice(s)


##############
# Extensions #
##############


class ShortThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at most 3 places away."""

    name = 'Short'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 4
    food_cost = 2
    max_range = 3
    implemented = True  # Change to True to view in the GUI
    # END Problem 4


class LongThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at least 5 places away."""

    name = 'Long'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 4
    food_cost = 2
    min_range = 5
    implemented = True  # Change to True to view in the GUI
    # END Problem 4


class FireAnt(Ant):
    """FireAnt cooks any Bee in its Place when it expires."""

    name = 'Fire'
    damage = 3
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 5
    food_cost = 5
    implemented = True  # Change to True to view in the GUI

    # END Problem 5

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the FireAnt from its place if it
        has no armor remaining. If the FireAnt dies, damage each of the bees in
        the current place.
        """
        # BEGIN Problem 5
        "*** YOUR CODE HERE ***"
        self.armor -= amount
        if self.armor <= 0:
            for bee in list(self.place.bees):
                bee.reduce_armor(self.damage)
            self.place.remove_insect(self)
        # END Problem 5


class HungryAnt(Ant):
    """HungryAnt will take three turns to digest a Bee in its place.
    While digesting, the HungryAnt can't eat another Bee.
    """
    name = 'Hungry'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 6
    food_cost = 4
    time_to_digest = 3
    implemented = True  # Change to True to view in the GUI

    # END Problem 6

    def __init__(self, armor=1):
        # BEGIN Problem 6
        "*** YOUR CODE HERE ***"
        super().__init__(armor)
        self.digesting = 0
        # END Problem 6

    def eat_bee(self, bee):
        # BEGIN Problem 6
        "*** YOUR CODE HERE ***"
        bee.reduce_armor(bee.armor)
        # END Problem 6

    def action(self, colony):
        # BEGIN Problem 6
        "*** YOUR CODE HERE ***"
        if self.digesting > 0:
            self.digesting -= 1
            return
        if len(self.place.bees) > 0:
            self.eat_bee(random.choice(self.place.bees))
            self.digesting = self.time_to_digest
        # END Problem 6


class NinjaAnt(Ant):
    """NinjaAnt does not block the path and damages all bees in its place."""

    name = 'Ninja'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 7
    food_cost = 5
    blocks_path = False
    implemented = True  # Change to True to view in the GUI

    # END Problem 7

    def action(self, colony):
        # BEGIN Problem 7
        "*** YOUR CODE HERE ***"
        for bee in list(self.place.bees):
            bee.reduce_armor(self.damage)
        # END Problem 7


# BEGIN Problem 8
# The WallAnt class
class WallAnt(Ant):
    name = "Wall"
    food_cost = 4
    implemented = True

    def __init__(self, armor=4):
        super().__init__(armor)


# END Problem 8


class BodyguardAnt(Ant):
    """BodyguardAnt provides protection to other Ants."""

    name = 'Bodyguard'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 9
    food_cost = 4
    is_container = True
    implemented = True  # Change to True to view in the GUI

    # END Problem 9

    def __init__(self, armor=2):
        Ant.__init__(self, armor)
        self.contained_ant = None  # The Ant hidden in this bodyguard

    def can_contain(self, other):
        # BEGIN Problem 9
        "*** YOUR CODE HERE ***"
        return self.contained_ant is None and not other.is_container
        # END Problem 9

    def contain_ant(self, ant):
        # BEGIN Problem 9
        "*** YOUR CODE HERE ***"
        self.contained_ant = ant
        # END Problem 9

    def action(self, colony):
        # BEGIN Problem 9
        "*** YOUR CODE HERE ***"
        if self.contained_ant is not None:
            self.contained_ant.action(colony)
        # END Problem 9


class TankAnt(BodyguardAnt):
    """TankAnt provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 10
    food_cost = 6
    is_container = True
    implemented = True  # Change to True to view in the GUI

    # END Problem 10

    def action(self, colony):
        # BEGIN Problem 10
        "*** YOUR CODE HERE ***"
        super().action(colony)
        for bee in list(self.place.bees):
            bee.reduce_armor(self.damage)
        # END Problem 10


class Water(Place):
    """Water is a place that can only hold watersafe insects."""
    def add_insect(self, insect):
        """Add an Insect to this place. If the insect is not watersafe, reduce
        its armor to 0."""
        # BEGIN Problem 11
        "*** YOUR CODE HERE ***"
        super().add_insect(insect)
        if not insect.is_watersafe:
            insect.reduce_armor(insect.armor)
        # END Problem 11


# BEGIN Problem 12
# The ScubaThrower class
class ScubaThrower(ThrowerAnt):
    name = 'Scuba'
    food_cost = 6
    is_watersafe = True
    implemented = True


# END Problem 12


# BEGIN Problem 13
class QueenAnt(ScubaThrower):  # You should change this line
    # END Problem 13
    """The Queen of the colony. The game is over if a bee enters her place."""

    name = 'Queen'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem 13
    food_cost = 7
    is_true_queen = True
    implemented = True  # Change to True to view in the GUI

    # END Problem 13

    def __init__(self, armor=1):
        # BEGIN Problem 13
        "*** YOUR CODE HERE ***"
        super().__init__(armor)
        self.is_true_queen = QueenAnt.is_true_queen
        if QueenAnt.is_true_queen:
            QueenAnt.is_true_queen = False
        self.buffed_ants = []
        # END Problem 13

    def buff_ant(self, ant):
        if ant not in self.buffed_ants:
            ant.damage *= 2
            self.buffed_ants.append(ant)

    def buff_ants_start_from(self, place):
        if place is None:
            return
        current_ant = place.ant
        if current_ant is not None:
            self.buff_ant(current_ant)
            if current_ant.is_container:
                contained_ant = current_ant.contained_ant
                if contained_ant is not None:
                    self.buff_ant(contained_ant)
        self.buff_ants_start_from(place.exit)

    def action(self, colony):
        """A queen ant throws a leaf, but also doubles the damage of ants
        in her tunnel.

        Impostor queens do only one thing: reduce their own armor to 0.
        """
        # BEGIN Problem 13
        "*** YOUR CODE HERE ***"
        if not self.is_true_queen:
            self.reduce_armor(self.armor)
            return
        super().action(colony)
        for ant in list(self.buffed_ants):
            if ant.armor <= 0:
                self.buffed_ants.remove(ant)
        self.buff_ants_start_from(self.place.exit)
        # END Problem 13

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True QueenAnt has no armor
        remaining, signal the end of the game.
        """
        # BEGIN Problem 13
        "*** YOUR CODE HERE ***"
        super().reduce_armor(amount)
        if self.armor <= 0 and self.is_true_queen:
            bees_win()
        # END Problem 13


class AntRemover(Ant):
    """Allows the player to remove ants from the board in the GUI."""

    name = 'Remover'
    implemented = False

    def __init__(self):
        Ant.__init__(self, 0)


##################
# Status Effects #
##################


def make_slow(action, bee):
    """Return a new action method that calls ACTION every other turn.

    action -- An action method of some Bee
    """
    # BEGIN Problem EC
    "*** YOUR CODE HERE ***"

    def slow_action(colony):
        if colony.time % 2 == 0:
            action(colony)

    return slow_action
    # END Problem EC


def make_scare(action, bee):
    """Return a new action method that makes the bee go backwards.

    action -- An action method of some Bee
    """
    # BEGIN Problem EC
    "*** YOUR CODE HERE ***"

    def scared_action(colony):
        bee.is_scared = True
        action(colony)
        bee.is_scared = False

    return scared_action
    # END Problem EC


def apply_effect(effect, bee, duration):
    """Apply a status effect to a BEE that lasts for DURATION turns."""
    # BEGIN Problem EC
    "*** YOUR CODE HERE ***"
    original_action = bee.action

    def effect_action(colony):
        nonlocal duration
        if duration > 0:
            effect(original_action, bee)(colony)
            duration -= 1
        else:
            original_action(colony)
            bee.action = original_action

    bee.action = effect_action
    # END Problem EC


class SlowThrower(ThrowerAnt):
    """ThrowerAnt that causes Slow on Bees."""

    name = 'Slow'
    # BEGIN Problem EC
    food_cost = 4
    implemented = True  # Change to True to view in the GUI

    # END Problem EC

    def throw_at(self, target):
        if target is not None:
            apply_effect(make_slow, target, 3)


class ScaryThrower(ThrowerAnt):
    """ThrowerAnt that intimidates Bees, making them back away instead of advancing."""

    name = 'Scary'
    # BEGIN Problem EC
    food_cost = 6
    implemented = True  # Change to True to view in the GUI

    # END Problem EC

    def throw_at(self, target):
        # BEGIN Problem EC
        "*** YOUR CODE HERE ***"
        if target is not None and not target.scared_once:
            apply_effect(make_scare, target, 2)
            target.scared_once = True
        # END Problem EC


class LaserAnt(ThrowerAnt):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN Problem OPTIONAL
    damage = 2
    food_cost = 10
    implemented = True  # Change to True to view in the GUI

    # END Problem OPTIONAL

    def __init__(self, armor=1):
        ThrowerAnt.__init__(self, armor)
        self.insects_shot = 0

    def insects_in_front(self, hive):
        # BEGIN Problem OPTIONAL
        insects = dict()

        def find_insects_in_front_start_from(place, distance=0):
            if place is None:
                return insects
            current_ant = place.ant
            if current_ant is not None and current_ant is not self:
                insects[current_ant] = distance
                if current_ant.is_container:
                    contained_ant = current_ant.contained_ant
                    if contained_ant is not None:
                        insects[contained_ant] = distance
            if len(place.bees) > 0:
                for bee in place.bees:
                    insects[bee] = distance
            return find_insects_in_front_start_from(place.entrance,
                                                    distance + 1)

        find_insects_in_front_start_from(self.place)
        return insects
        # END Problem OPTIONAL

    def calculate_damage(self, distance):
        # BEGIN Problem OPTIONAL
        return self.damage - distance * 0.2 - self.insects_shot * 0.05
        # END Problem OPTIONAL

    def action(self, colony):
        insects_and_distances = self.insects_in_front(colony.hive)
        for insect, distance in insects_and_distances.items():
            damage = self.calculate_damage(distance)
            insect.reduce_armor(damage)
            if damage:
                self.insects_shot += 1


##################
# Bees Extension #
##################


class Wasp(Bee):
    """Class of Bee that has higher damage."""
    name = 'Wasp'
    damage = 2


class Hornet(Bee):
    """Class of bee that is capable of taking two actions per turn, although
    its overall damage output is lower. Immune to status effects.
    """
    name = 'Hornet'
    damage = 0.25

    def action(self, colony):
        for i in range(2):
            if self.armor > 0:
                super().action(colony)

    def __setattr__(self, name, value):
        if name != 'action':
            object.__setattr__(self, name, value)


class NinjaBee(Bee):
    """A Bee that cannot be blocked. Is capable of moving past all defenses to
    assassinate the Queen.
    """
    name = 'NinjaBee'

    def blocked(self):
        return False


class Boss(Wasp, Hornet):
    """The leader of the bees. Combines the high damage of the Wasp along with
    status effect immunity of Hornets. Damage to the boss is capped up to 8
    damage by a single attack.
    """
    name = 'Boss'
    damage_cap = 8
    action = Wasp.action

    def reduce_armor(self, amount):
        super().reduce_armor(self.damage_modifier(amount))

    def damage_modifier(self, amount):
        return amount * self.damage_cap / (self.damage_cap + amount)


class Hive(Place):
    """The Place from which the Bees launch their assault.

    assault_plan -- An AssaultPlan; when & where bees enter the colony.
    """
    def __init__(self, assault_plan):
        self.name = 'Hive'
        self.assault_plan = assault_plan
        self.bees = []
        for bee in assault_plan.all_bees:
            self.add_insect(bee)
        # The following attributes are always None for a Hive
        self.entrance = None
        self.ant = None
        self.exit = None

    def strategy(self, colony):
        exits = [p for p in colony.places.values() if p.entrance is self]
        for bee in self.assault_plan.get(colony.time, []):
            bee.move_to(random.choice(exits))
            colony.active_bees.append(bee)


class AntColony(object):
    """An ant collective that manages global game state and simulates time.

    Attributes:
    time -- elapsed time
    food -- the colony's available food total
    queen -- the place where the queen resides
    places -- A list of all places in the colony (including a Hive)
    bee_entrances -- A list of places that bees can enter
    """
    def __init__(self,
                 strategy,
                 hive,
                 ant_types,
                 create_places,
                 dimensions,
                 food=2):
        """Create an AntColony for simulating a game.

        Arguments:
        strategy -- a function to deploy ants to places
        hive -- a Hive full of bees
        ant_types -- a list of ant constructors
        create_places -- a function that creates the set of places
        dimensions -- a pair containing the dimensions of the game layout
        """
        self.time = 0
        self.food = food
        self.strategy = strategy
        self.hive = hive
        self.ant_types = OrderedDict((a.name, a) for a in ant_types)
        self.dimensions = dimensions
        self.active_bees = []
        self.configure(hive, create_places)

    def configure(self, hive, create_places):
        """Configure the places in the colony."""
        self.queen = QueenPlace('AntQueen')
        self.places = OrderedDict()
        self.bee_entrances = []

        def register_place(place, is_bee_entrance):
            self.places[place.name] = place
            if is_bee_entrance:
                place.entrance = hive
                self.bee_entrances.append(place)

        register_place(self.hive, False)
        create_places(self.queen, register_place, self.dimensions[0],
                      self.dimensions[1])

    def simulate(self):
        """Simulate an attack on the ant colony (i.e., play the game)."""
        num_bees = len(self.bees)
        try:
            while True:
                self.hive.strategy(self)  # Bees invade
                self.strategy(self)  # Ants deploy
                for ant in self.ants:  # Ants take actions
                    if ant.armor > 0:
                        ant.action(self)
                for bee in self.active_bees[:]:  # Bees take actions
                    if bee.armor > 0:
                        bee.action(self)
                    if bee.armor <= 0:
                        num_bees -= 1
                        self.active_bees.remove(bee)
                if num_bees == 0:
                    raise AntsWinException()
                self.time += 1
        except AntsWinException:
            print('All bees are vanquished. You win!')
            return True
        except BeesWinException:
            print('The ant queen has perished. Please try again.')
            return False

    def deploy_ant(self, place_name, ant_type_name):
        """Place an ant if enough food is available.

        This method is called by the current strategy to deploy ants.
        """
        constructor = self.ant_types[ant_type_name]
        if self.food < constructor.food_cost:
            print('Not enough food remains to place ' + ant_type_name)
        else:
            ant = constructor()
            self.places[place_name].add_insect(ant)
            self.food -= constructor.food_cost
            return ant

    def remove_ant(self, place_name):
        """Remove an Ant from the Colony."""
        place = self.places[place_name]
        if place.ant is not None:
            place.remove_insect(place.ant)

    @property
    def ants(self):
        return [p.ant for p in self.places.values() if p.ant is not None]

    @property
    def bees(self):
        return [b for p in self.places.values() for b in p.bees]

    @property
    def insects(self):
        return self.ants + self.bees

    def __str__(self):
        status = ' (Food: {0}, Time: {1})'.format(self.food, self.time)
        return str([str(i) for i in self.ants + self.bees]) + status


class QueenPlace(Place):
    """QueenPlace at the end of the tunnel, where the queen resides."""
    def add_insect(self, insect):
        """Add an Insect to this Place.

        Can't actually add Ants to a QueenPlace. However, if a Bee attempts to
        enter the QueenPlace, a BeesWinException is raised, signaling the end
        of a game.
        """
        assert not insect.is_ant, 'Cannot add {0} to QueenPlace'
        raise BeesWinException()


def ants_win():
    """Signal that Ants win."""
    raise AntsWinException()


def bees_win():
    """Signal that Bees win."""
    raise BeesWinException()


def ant_types():
    """Return a list of all implemented Ant classes."""
    all_ant_types = []
    new_types = [Ant]
    while new_types:
        new_types = [t for c in new_types for t in c.__subclasses__()]
        all_ant_types.extend(new_types)
    return [t for t in all_ant_types if t.implemented]


class GameOverException(Exception):
    """Base game over Exception."""
    pass


class AntsWinException(GameOverException):
    """Exception to signal that the ants win."""
    pass


class BeesWinException(GameOverException):
    """Exception to signal that the bees win."""
    pass


def interactive_strategy(colony):
    """A strategy that starts an interactive session and lets the user make
    changes to the colony.

    For example, one might deploy a ThrowerAnt to the first tunnel by invoking
    colony.deploy_ant('tunnel_0_0', 'Thrower')
    """
    print('colony: ' + str(colony))
    msg = '<Control>-D (<Control>-Z <Enter> on Windows) completes a turn.\n'
    interact(msg)


def start_with_strategy(args, strategy):
    """Reads command-line arguments and starts a game with those options."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Ants vs. SomeBees")
    parser.add_argument(
        '-d',
        type=str,
        metavar='DIFFICULTY',
        help='sets difficulty of game (test/easy/medium/hard/extra-hard)')
    parser.add_argument('-w',
                        '--water',
                        action='store_true',
                        help='loads a full layout with water')
    parser.add_argument('--food',
                        type=int,
                        help='number of food to start with when testing',
                        default=2)
    args = parser.parse_args()

    assault_plan = make_normal_assault_plan()
    layout = dry_layout
    tunnel_length = 9
    num_tunnels = 3
    food = args.food

    if args.water:
        layout = wet_layout
    if args.d in ['t', 'test']:
        assault_plan = make_test_assault_plan()
        num_tunnels = 1
    elif args.d in ['e', 'easy']:
        assault_plan = make_easy_assault_plan()
        num_tunnels = 2
    elif args.d in ['n', 'normal']:
        assault_plan = make_normal_assault_plan()
        num_tunnels = 3
    elif args.d in ['h', 'hard']:
        assault_plan = make_hard_assault_plan()
        num_tunnels = 4
    elif args.d in ['i', 'extra-hard']:
        assault_plan = make_extra_hard_assault_plan()
        num_tunnels = 4

    hive = Hive(assault_plan)
    dimensions = (num_tunnels, tunnel_length)
    return AntColony(strategy, hive, ant_types(), layout, dimensions,
                     food).simulate()


###########
# Layouts #
###########


def wet_layout(queen, register_place, tunnels=3, length=9, moat_frequency=3):
    """Register a mix of wet and and dry places."""
    for tunnel in range(tunnels):
        exit = queen
        for step in range(length):
            if moat_frequency != 0 and (step + 1) % moat_frequency == 0:
                exit = Water('water_{0}_{1}'.format(tunnel, step), exit)
            else:
                exit = Place('tunnel_{0}_{1}'.format(tunnel, step), exit)
            register_place(exit, step == length - 1)


def dry_layout(queen, register_place, tunnels=3, length=9):
    """Register dry tunnels."""
    wet_layout(queen, register_place, tunnels, length, 0)


#################
# Assault Plans #
#################


class AssaultPlan(dict):
    """The Bees' plan of attack for the Colony.  Attacks come in timed waves.

    An AssaultPlan is a dictionary from times (int) to waves (list of Bees).

    >>> AssaultPlan().add_wave(4, 2)
    {4: [Bee(3, None), Bee(3, None)]}
    """
    def add_wave(self, bee_type, bee_armor, time, count):
        """Add a wave at time with count Bees that have the specified armor."""
        bees = [bee_type(bee_armor) for _ in range(count)]
        self.setdefault(time, []).extend(bees)
        return self

    @property
    def all_bees(self):
        """Place all Bees in the hive and return the list of Bees."""
        return [bee for wave in self.values() for bee in wave]


def make_test_assault_plan():
    return AssaultPlan().add_wave(Bee, 3, 2, 1).add_wave(Bee, 3, 3, 1)


def make_easy_assault_plan():
    plan = AssaultPlan()
    for time in range(3, 16, 2):
        plan.add_wave(Bee, 3, time, 1)
    plan.add_wave(Wasp, 3, 4, 1)
    plan.add_wave(NinjaBee, 3, 8, 1)
    plan.add_wave(Hornet, 3, 12, 1)
    plan.add_wave(Boss, 15, 16, 1)
    return plan


def make_normal_assault_plan():
    plan = AssaultPlan()
    for time in range(3, 16, 2):
        plan.add_wave(Bee, 3, time, 2)
    plan.add_wave(Wasp, 3, 4, 1)
    plan.add_wave(NinjaBee, 3, 8, 1)
    plan.add_wave(Hornet, 3, 12, 1)
    plan.add_wave(Wasp, 3, 16, 1)

    #Boss Stage
    for time in range(21, 30, 2):
        plan.add_wave(Bee, 3, time, 2)
    plan.add_wave(Wasp, 3, 22, 2)
    plan.add_wave(Hornet, 3, 24, 2)
    plan.add_wave(NinjaBee, 3, 26, 2)
    plan.add_wave(Hornet, 3, 28, 2)
    plan.add_wave(Boss, 20, 30, 1)
    return plan


def make_hard_assault_plan():
    plan = AssaultPlan()
    for time in range(3, 16, 2):
        plan.add_wave(Bee, 4, time, 2)
    plan.add_wave(Hornet, 4, 4, 2)
    plan.add_wave(Wasp, 4, 8, 2)
    plan.add_wave(NinjaBee, 4, 12, 2)
    plan.add_wave(Wasp, 4, 16, 2)

    #Boss Stage
    for time in range(21, 30, 2):
        plan.add_wave(Bee, 4, time, 3)
    plan.add_wave(Wasp, 4, 22, 2)
    plan.add_wave(Hornet, 4, 24, 2)
    plan.add_wave(NinjaBee, 4, 26, 2)
    plan.add_wave(Hornet, 4, 28, 2)
    plan.add_wave(Boss, 30, 30, 1)
    return plan


def make_extra_hard_assault_plan():
    plan = AssaultPlan()
    plan.add_wave(Hornet, 5, 2, 2)
    for time in range(3, 16, 2):
        plan.add_wave(Bee, 5, time, 2)
    plan.add_wave(Hornet, 5, 4, 2)
    plan.add_wave(Wasp, 5, 8, 2)
    plan.add_wave(NinjaBee, 5, 12, 2)
    plan.add_wave(Wasp, 5, 16, 2)

    #Boss Stage
    for time in range(21, 30, 2):
        plan.add_wave(Bee, 5, time, 3)
    plan.add_wave(Wasp, 5, 22, 2)
    plan.add_wave(Hornet, 5, 24, 2)
    plan.add_wave(NinjaBee, 5, 26, 2)
    plan.add_wave(Hornet, 5, 28, 2)
    plan.add_wave(Boss, 30, 30, 2)
    return plan


from utils import *


@main
def run(*args):
    Insect.reduce_armor = class_method_wrapper(Insect.reduce_armor,
                                               pre=print_expired_insects)
    start_with_strategy(args, interactive_strategy)
