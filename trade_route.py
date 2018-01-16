import random
from heapq import nlargest
from collections import namedtuple, defaultdict


Item       = namedtuple('Item', 'dest,price')
ShipConfig = namedtuple('ShipConfig', 'mesh,capacity,cost_per_au')

def nlg_key(item):
    return item.price
class Ship:
    def __init__(self, config, planet, items, history=[]):
        self.config = config
        self.planet = planet
        self.items = set(items)
        self.history = history

    @property
    def to_unload(self):
        """Set of items to unload at the current planet."""
        return {i for i in self.items if i.dest == self.planet}

    def load_value(self, planet, route):
        """
        Load the ship based purely on max credit value of shipments
        to any planets in the rest of the route

        planet - The planet the ship will load shipments
        route - The route from this planet forward
        """
        route_names = []
        for p in route:
            route_names.append(p.id)

        to_load = set(nlargest(  # be greedy and load the most valuable items
            self.config.capacity - len(self.items),
            [i for i in planet.items if i.dest.id in route_names], key=nlg_key))

        #
        # Consume the loaded items
        #
        for i in to_load:
            planet.items.remove(i)

        self.items |= to_load
        return to_load

    def unload_new(self, planet):
        sell = [i for i in self.items if i.dest == planet]
        gain = 0
        #
        # Consume the sold items
        #
        for i in sell:
            self.items.remove(i)
            gain += i.price

        return gain, sell


    def unload(self):
        """
        Unload the ship in the current planet. Returns a new
        ship and the gain from unloading cargo.
        """
        ship = Ship(
            self.config,
            self.planet,
            self.items - self.to_unload,
            self.history
            )
        gain = sum(i.price for i in self.to_unload)
        return ship, gain

    def load_move(self, planet, items):
        """
        Unload the current ship, load items from *items* with dest
        *planet* and move it to *planet*.
        """
        to_load = set(nlargest(  # be greedy and load the most valuable items
            self.config.capacity - len(self.items),
            [i for i in items if i.dest is planet],
            ))
        ship = Ship(
            self.config,
            planet,
            self.items | to_load,
            self.history + [planet],
            )
        return ship, items - to_load

    def cost_to(self, planet):
        """Hydrogen cost to move from this planet to the given *planet*."""
        pq = frozenset([planet, self.planet])
        dist = self.config.mesh[pq]
        cost = self.config.cost_per_au
        return dist * cost


class Planet:
    __slots__ = ('id', 'items')

    def __init__(self, id, items):
        self.id = id
        self.items = items

    def __repr__(self):
        return 'Planet(%r)' % (self.id,)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def copy(self):
        cp_items = self.items[:]
        return Planet(self.id, cp_items)


    def with_items(self, iv):
        return Planet(self.id, items)


def find_path(planets, ship, hydrogen, k,
        gain_weight=1.0, # weighting for credit gain, ++ if aiming to maximise
        cost_weight=1.0, # weighting for hydrogen use, ++ if aiming to conserve
        ):
    total_gain = 0
    total_cost = 0
    route = [ship.planet]
    shipments = {p: set(p.items) for p in planets}

    def f(x):
        g, c, _, _ = x
        return gain_weight * g - cost_weight * c

    # while we still have fuel
    while hydrogen > 0:
        R = kfind(shipments, ship, hydrogen, k)
#        print ("==============================")
        if not R:
            break
        gain, cost, ship, shipments = max(R, key=f)
#        print ("gain:{}, cost:{}".format(gain, cost))
        hydrogen -= cost
        total_gain += gain
        total_cost += cost
        route.extend(ship.history)
        ship.history = []

    return route, total_gain, total_cost


def _move(ship, planet, shipments):
    src = ship.planet 
    S = shipments.copy()
    ship, S[src] = ship.load_move(planet, shipments[src])
    return ship, S


def kfind(shipments, ship, hydrogen, k):
    route = []
    q = [(0, shipments, 0, 0, ship)]

    while q:
        step, shipments, gain, cost, ship = q.pop()
#        print ("Dest{} /{} : {}".format(ship.planet, cost, ship.to_unload))
#        thing = raw_input('continue?')

        if cost > hydrogen:
            continue

        ship, g = ship.unload()
#        print ("Unload: {}".format(g))
        gain += g
        # if we've ran out of lookahead steps, shipments or
        # hydrogen then push this to the solution space
        if not any(shipments.values()) or step == k or \
                cost == hydrogen:

            if not ship.history:
                continue
            if gain == 0:
                continue
            #print(''.join(p.id for p in ship.history), gain - cost)
            route.append((gain, cost, ship, shipments))
            continue

        for planet in shipments:
            if planet == ship.planet:
                continue
            # load items from the current planet and move to the
            # new planet
            new_ship, new_shipments = _move(ship, planet, shipments)
            q.append((
                step + 1,
                new_shipments,
                gain,
                cost + ship.cost_to(planet),
                new_ship,
                ))

#    print('---')
    return [(g, c, s, S) for g, c, s, S in route]

class Node():
    def __init__(self, planet):
        self.planet = planet
        self.dests = []





# def mfind(ship, planets):

#     route = []
#     limit = 2
#     tree = Node(ship.planet)
#     nodelist = [tree]

#     build_to_k(node)

#     while limit:

#         for node in nodelist:
#             for planet in planets:
#                 cur_node.dests.append(Node(planet))

#         limit -= 1




#             #
#             # Find the dest with the best C/hydro ratio
#             #
#             load = set(nlargest(  # be greedy and load the most valuable items
#                 ship.config.capacity - len(ship.items),
#                 [i for i in ship.planet.items if i.dest is planet],
#                 ))
#             cost = ship.cost_to(planet)
#             gain = sum(i.price for i in load)
#             print (load)
#             print (cost)
#             print (gain/cost)

