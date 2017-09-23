from trade_route import *

p = lambda a,b: frozenset([a,b])

A  = Planet('A',  [])
A1 = Planet('A1', [])
V  = Planet('V',  [])
V1 = Planet('V1', [])
B  = Planet('B',  [])
B1 = Planet('B1', [])
B2 = Planet('B2', [])
M  = Planet('M',  [])

A.items = [
    Item(A1, 20),
    Item(B,  75),
    Item(B1, 42),
    Item(B1, 86),
    Item(M,  63),
]
A1.items = [
    Item(A, 6),
    Item(B, 71),
    Item(B2, 101),
    Item(B2, 124),
    Item(M, 66),
]
V.items = [
    Item(V1, 21),
    Item(V1, 8),
    Item(A1, 43),
    Item(A1, 45),
    Item(B1, 64),
    Item(B2, 102),
]
V1.items = [
    Item(A1, 44),
    Item(A1, 45),
    Item(B,  78),
    Item(B1, 166),
    Item(B2, 65),
    Item(B2, 65),
]
M.items = [
    Item(B1, 189),
    Item(V1, 101),
    Item(V1, 190),
    Item(V1, 90),
    Item(B2, 110),
    Item(V,  100),
]


config = ShipConfig(
        defaultdict(lambda: float('inf'), {
            p(M,  B1): 573,
            p(M,  V1): 599,
            p(M,  B2): 657,
            p(M,  V):  678,
            p(V1, A1): 547,
            p(V1, B):  708,
            p(V1, B1): 747,
            p(V1, B2): 829,
            p(V,  V1): 96,
            p(V,  A1): 612,
            p(V,  B1): 842,
            p(V,  B2): 923,
            p(A,  A1): 65,
            p(A,  B):  399,
            p(A,  B1): 465,
            p(A,  M):  835,
            p(A1, B):  418,
            p(A1, B2): 515,
            p(A1, M):  806,
            }),
        3,
        0.068,
        )


k = 2
route, gain, cost = find_path(
    [A, A1, B, B1, B2, V, V1, M],
    Ship(config, A, set()),
    1691,
    k,
    )
print('Arms:', k)
print(' '.join(p.id for p in route))
print('Length: ', len(route))
print('Gain:', gain)
print('Cost:', cost)
