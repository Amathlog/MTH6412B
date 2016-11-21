# -*- coding: utf-8 -*-

from algoMST import prim, kruskal
from MST import MST

def solveTSP(g, source, algoPrim = True):

    if algoPrim:
        mst = prim(g, source)
    else:
        mst = kruskal(g)

    exploring = [source]
    notVisited = [value for value in g.get_nodes()]
    travel = MST(g)

    while len(exploring) != 0:
        curr = exploring.pop(0)
        notVisited.remove(curr)
        exploring = [value for value in notVisited if (curr, value) in mst.get_adj_matrix()] + exploring
        if len(exploring) == 0:
            travel.add_edge(g.get_adj_matrix()[(curr, source)])
        else:
            travel.add_edge(g.get_adj_matrix()[(curr, exploring[0])])

    return travel