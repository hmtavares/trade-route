from trade_route import *
import copy
import sys


#
# Shortcut to create a frozen set
#
p = lambda a,b: frozenset([a,b])

Amaral = Planet('Amaral', [])
Badger  = Planet('Badger',  [])
Codie  = Planet('Codie',  [])
Codie1 = Planet('Codie I', [])
Codie2  = Planet('Codie II',  [])
Mirvana = Planet('Mirvana', [])
Mirvana1 = Planet('Mirvana I', [])
Nox = Planet('Nox', [])
Zandalus = Planet('Zandalus', [])
Zandalus1 = Planet('Zandalus I', [])

planet_list = [
    Amaral,
    Badger,
    Codie,
    Codie1,
    Codie2,
    Mirvana,
    Mirvana1,
    Nox,
    Zandalus,
    Zandalus1
]

config = ShipConfig(
        defaultdict(lambda: float('inf'), {
            p(Amaral,  Badger): 644,
            p(Amaral,  Codie): 509,
            p(Amaral,  Codie1): 430,
            p(Amaral,  Codie2): 378,
            p(Amaral,  Mirvana): 882,
            p(Amaral,  Mirvana1): 794,
            p(Amaral,  Nox): 1704,
            p(Amaral,  Zandalus): 1379,
            p(Amaral,  Zandalus1): 1358,

            p(Badger,  Codie): 1042,
            p(Badger,  Codie1): 987,
            p(Badger,  Codie2): 932,
            p(Badger,  Mirvana): 1305,
            p(Badger,  Mirvana1): 1219,
            p(Badger,  Nox): 2245,
            p(Badger,  Zandalus): 1803,
            p(Badger,  Zandalus1): 1743,

            p(Codie,  Codie1): 83,
            p(Codie,  Codie2): 130,
            p(Codie,  Mirvana): 399,
            p(Codie,  Mirvana1): 321,
            p(Codie,  Nox): 1212,
            p(Codie,  Zandalus): 875,
            p(Codie,  Zandalus1): 868,

            p(Codie1,  Codie2): 55,
            p(Codie1,  Mirvana): 480,
            p(Codie1,  Mirvana1): 402,
            p(Codie1,  Nox): 1281,
            p(Codie1,  Zandalus): 959,
            p(Codie1,  Zandalus1): 952,

            p(Codie2,  Mirvana): 520,
            p(Codie2,  Mirvana1): 436,
            p(Codie2,  Nox): 1336,
            p(Codie2,  Zandalus): 1004,
            p(Codie2,  Zandalus1): 993,

            p(Mirvana,  Mirvana1): 89,
            p(Mirvana,  Nox): 976,
            p(Mirvana,  Zandalus): 505,
            p(Mirvana,  Zandalus1): 475,

            p(Mirvana1,  Nox): 1049,
            p(Mirvana1,  Zandalus): 595,
            p(Mirvana1,  Zandalus1): 564,

            p(Nox,  Zandalus): 618,
            p(Nox,  Zandalus1): 757,

            p(Zandalus,  Zandalus1): 130,
            }),
        8,
        0.2,
        )

# item(destination, credit value)
Amaral.items = [
    Item(Codie1, 227),
    Item(Codie1, 96),
    Item(Codie, 282),
    Item(Codie, 87),
    Item(Badger, 124),
    Item(Badger, 111),
    Item(Mirvana, 269),
    Item(Mirvana, 183),
    Item(Mirvana, 191),
    Item(Mirvana, 83),
    Item(Mirvana, 171),
    Item(Mirvana, 206),
    Item(Zandalus1, 305),
    Item(Zandalus1, 214),
    Item(Zandalus, 276),
    Item(Nox, 187),
    Item(Nox, 303),
    Item(Nox, 161),
]
Badger.items = [
    Item(Codie2, 112),
    Item(Codie2, 112),
    Item(Codie2, 123),
    Item(Codie1, 157),
    Item(Codie1, 153),
    Item(Codie1, 144),
    Item(Codie, 162),
    Item(Mirvana1, 155),
    Item(Mirvana, 164),
    Item(Mirvana, 167),
    Item(Mirvana, 175),
    Item(Zandalus1, 195),
    Item(Zandalus1, 281),
    Item(Nox, 180),
    Item(Nox, 218),
]

Codie.items = [
    Item(Codie2, 9),
    Item(Mirvana1, 48),
    Item(Badger, 83),
    Item(Badger, 123),
    Item(Nox, 90),
    Item(Nox, 64),

]

Codie1.items = [
    Item(Codie2, 4),
    Item(Mirvana1, 43),
    Item(Amaral, 55),
    Item(Zandalus, 78),
    Item(Zandalus, 55),
    Item(Badger, 70),
]


Codie2.items = [
    Item(Codie1, 6),
    Item(Amaral, 73),
    Item(Amaral, 198),
    Item(Amaral, 179),
    Item(Amaral, 106),
    Item(Amaral, 143),
    Item(Mirvana, 70),
    Item(Badger, 91),
    Item(Badger, 79),
    Item(Badger, 54),

]

Mirvana.items = [
    Item(Mirvana1, 35),
    Item(Codie, 67),
    Item(Zandalus1, 82),
    Item(Zandalus1, 189),
    Item(Codie1, 115),
    Item(Zandalus, 143),
    Item(Zandalus, 144),
    Item(Zandalus, 38),
    Item(Zandalus, 55),
    Item(Nox, 75),
    Item(Nox, 110),

]

Mirvana1.items = [
    Item(Codie, 31),
    Item(Codie, 87),
    Item(Codie, 82),
    Item(Codie1, 91),
    Item(Codie1, 178),
    Item(Codie2, 43),
    Item(Zandalus1, 68),
    Item(Zandalus1, 114),
    Item(Zandalus1, 53),
    Item(Zandalus, 203),
    Item(Nox, 164),
    Item(Nox, 231),
    Item(Badger, 230),

]

Nox.items = [
    Item(Zandalus, 97),
    Item(Zandalus, 149),
    Item(Zandalus, 101),
    Item(Zandalus1, 48),
    Item(Zandalus, 153),
    Item(Mirvana, 111),
    Item(Mirvana, 152),
    Item(Mirvana, 92),
    Item(Mirvana, 148),
    Item(Mirvana, 149),
    Item(Mirvana, 119),
    Item(Mirvana, 161),
    Item(Mirvana1, 99),
    Item(Mirvana1, 64),
    Item(Codie, 214),
    Item(Codie, 88),
    Item(Codie1, 203),
    Item(Codie1, 101),
    Item(Codie1, 166),
    Item(Codie1, 114),
    Item(Codie1, 89),
    Item(Codie2, 189),
    Item(Amaral, 129),
    Item(Amaral, 143),
    Item(Amaral, 171),
    Item(Badger, 185),
    Item(Badger, 153),

]

Zandalus.items = [
    Item(Zandalus1, 9),
    Item(Mirvana, 32),
    Item(Mirvana1, 36),
    Item(Nox, 94),
    Item(Nox, 53),
    Item(Nox, 67),
    Item(Nox, 42),
    Item(Nox, 102),
    Item(Codie, 65),
    Item(Codie, 67),
    Item(Codie1, 92),
    Item(Amaral, 118),
    Item(Amaral, 117),
]


Zandalus1.items = [
    Item(Zandalus, 7),
    Item(Mirvana, 49),
    Item(Mirvana, 36),
    Item(Mirvana, 39),
    Item(Codie1, 64),
    Item(Codie1, 77),
    Item(Amaral, 112),
    Item(Amaral, 98),
    Item(Amaral, 113),
    Item(Badger, 122),
    Item(Badger, 83),
    Item(Badger, 89),
]



my_ship = Ship(config, Codie, set())
#mfind(my_ship, planet_list)
#exit(0)

# k = 2

# route, gain, cost = find_path(
#     planet_list,
#     Ship(config, Codie, set()),
#     4000,
#     k,
#     )
# print('Arms:', k)
# print(' '.join(p.id for p in route))
# print('Length: ', len(route))
# print('Gain:', gain)
# print('Cost:', cost)



tree_planet_list = [
    Amaral,
    Badger,
    Codie
]

#
# build out the destination nodes for all the destinations in
# the parent node. The depth if each branch is limited to
# the number of 'steps' provided
#
# p_node: Parent Node. The node to add destinations to
# step: The steps/levels remaining in the branch. (including this one)
#
# Return: True - End reached. Stop recursion
#         False - Keep going
#
def build_to_k(p_node, step, planets):
    if step == 0:
#        print(" {}: {} - []]".format(step, p_node.planet.id))
#        print('-----')
        return True

    for planet in planets:
        if planet == p_node.planet:
            #
            # Don't add a dest to self
            #
            continue
        cur_node = Node(planet)
        p_node.dests.append(cur_node)
        # route_display = []
        # for r_node in p_node.dests:
        #     route_display.append(r_node.planet.id)

#        print(" {}: {} - {}".format(step, p_node.planet.id, route_display))
        build_to_k(cur_node, step-1, planets)
#        print ("....")



#
# build out the destination nodes for all the destinations in
# the parent node. Limit each branch to the amount of hydro
# provided. i.e. when a ship would run out of fuel, stop.

# p_node: Parent Node. The node to add destinations to
# hydro: The amount of hydro left to consume on this branch
#
# Return: True - End reached. Stop recursion
#         False - Keep going
#
def build_to_hk(p_node, step, hydro, planets):
    if step == 0:
#        print(" {}: {} - []]".format(step, p_node.planet.id))
#        print('-----')
        return True
#    the_line = input("hi")
    for planet in planets:
        if planet == p_node.planet:
            #
            # Don't add a dest to self
            #
            continue

        #
        # Can we get to this planet?
        #
        leg = frozenset([p_node.planet, planet])
        cost = config.mesh[leg]
        if cost == float('inf'):
            raise Exception("Bad Path: {} - {}".format(leg, dupe_route))
        cost *= config.cost_per_au

        hydro_left = hydro - cost
        if hydro_left < 0:
            #
            # Can't Make it
            #
            continue

        #
        # We made it! Add the planet to the branch
        #
        cur_node = Node(planet)
        p_node.dests.append(cur_node)

        # route_display = []
        # for r_node in p_node.dests:
        #     route_display.append(r_node.planet.id)
        # print(" {}: {} - {}".format(hydro, p_node.planet.id, route_display))


        build_to_hk(cur_node, step-1, hydro_left, planets)
        # print ("....")


def build_route(node, route, routes):
    if len(node.dests) == 0:
        routes.append(route)
        return True

    for d_node in node.dests:
        newroute = route[:]
        newroute.append(d_node.planet)
        build_route(d_node, newroute, routes)

def copy_planet(planet, planet_copies):
    dupe_planet = planet_copies.get(planet.id)
    if not dupe_planet:
        #
        #  Create dupe
        #
        dupe_planet = planet.copy()
        planet_copies[dupe_planet.id] = dupe_planet
    return dupe_planet

#
# 
#
def copy_route(route):
    #
    # Make a map of planets so if the same planet shows
    # up again in the route we get the same instance
    #
    planet_copies = {}
    new_route = []
    for planet in route:
        dupe_planet = copy_planet(planet, planet_copies)

        new_route.append(dupe_planet)

    return new_route

# TODO: Why is calc route different from build_route?
def calculate_route(node, route, routes):
    if len(node.dests) == 0:
        routes.append(route)
        return True

    for d_node in node.dests:
        newroute = route[:]
        newroute.append(d_node.planet)
        newroute = copy_route(newroute)
        calculate_route(d_node, newroute, routes)

tree = Node(Codie)


#build_to_k(tree, 3, planet_list)
print("Building Tree")
build_to_hk(tree, 5, 2500, planet_list)

print("Building Routes")
the_routes = []
build_route(tree, [], the_routes)
#calculate_route(tree, [], the_routes)
print (len(the_routes))
#
# Calculate the length/cost of each route
# ShipConfig = namedtuple('ShipConfig', 'mesh,capacity,cost_per_au')

RouteReport = namedtuple('RouteReport', 'income, cost, route')

route_costs = []
print (the_routes[0])
for route in the_routes:
    #
    # Each route gets its own copy of the
    # planet items
    #
#    planet_copy = copy.deepcopy(tree_planet_list)
#    planet_copy = copy_planets(tree_planet_list)
#    print(planet_copy[0].items)
    dupe_route  = copy_route(route)

    # When using calculate_route() dupe_route = route    
#    dupe_route = route

    cur_planet = Codie.copy()
    route_len = 0
    income = 0
    rest_route = dupe_route[:]
    for planet in dupe_route:
#        print("{} ".format(cur_planet.id), end="")

        #
        # fill the ship
        #
#        print("Arrive: {}".format(cur_planet.id))
#        print("Available Shipments:")
#        for s in cur_planet.items:
#            print("  {} - {}".format(s.dest.id, s.price))

        new_items = my_ship.load_value(cur_planet, rest_route)

#        print ("Picking up:")
#        for s in new_items:
#            print("  {} - {}".format(s.dest.id, s.price))

        #
        # Move to the planet
        # eat hydro
        #
#        print("Moving to from {} -> {}".format(cur_planet, planet))

        leg = frozenset([cur_planet, planet])
        dist = config.mesh[leg]
        if dist == float('inf'):
            raise Exception("{} - {}".format(leg, dupe_route))
        route_len += dist
        cost = route_len * config.cost_per_au
#        print("Moving to from {} -> {} - cost {}".format(cur_planet, planet, dist))
#        print("({})".format(int(cost)), end="")
        #
        # unload the ship
        # get paid
        # 
        gain, sold= my_ship.unload_new(planet)

#        print("({})".format(gain), end="")
        
        income += gain
#        print ("Sold:")
#        for s in sold:
#            print("  {} - {}".format(s.dest.id, s.price))


        cur_planet = planet

        #
        # Consume the planet we're on from the route
        #
        try:
            rest_route.remove(cur_planet)
        except ValueError:
            # Don't worry if the planet isn't there
            pass

#    print("{} X ".format(cur_planet.id))

    route_elem = RouteReport(income, cost, dupe_route)
#    print("length: {} income: {}".format(route_len, income))
    route_costs.append(route_elem)

# for route in route_costs:
#     for leg in route[0]:
#         print("{} ".format(leg.id), end="")
#     print ("dist: {}, income: {}, ratio: {}".format(route[1], route[2], route[2]/route[1]))


def get_route_dist(route):
    #
    # Return the distance for the route
    #
    return route.cost

def get_route_income(route):
    #
    # Return the distance for the route
    #
    return route.income

def get_route_ratio(route):
    #
    #  Return the credit/distance ratio
    #
    return route.income / route.cost

print("Distance:")
print("Max: {}".format(max(route_costs, key=get_route_dist)))
print("Min: {}".format(min(route_costs, key=get_route_dist)))

print()
print("Ratio")
max_ratio = max(route_costs, key=get_route_ratio)
min_ratio = min(route_costs, key=get_route_ratio)
print("Max: {} - {}".format(max_ratio.income / max_ratio.cost,
                            max(route_costs, key=get_route_ratio)))
print("Min: {} - {}".format(min_ratio.income / min_ratio.cost,
                            min(route_costs, key=get_route_ratio)))
print()
print("Income")
print("Max: {}".format(max(route_costs, key=get_route_income)))
print("Min: {}".format(min(route_costs, key=get_route_income)))

