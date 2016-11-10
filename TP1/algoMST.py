# -*- coding: utf-8 -*-

import numpy as np
import sys
from heapq import heappush, heappop
from unionFind import UnionFind
from MST import MST

# Algorithme de Kruskal
def kruskal(g):
    # Initialise le poids total à 0
    weight = 0

    # Initialise la structure d'Union Find
    uf = UnionFind()

    # Initialise l'arbre de poids minimum associé à g
    A = MST(g)

    # Crée un ensemble singleton pour chaque sommet
    for node in g.get_nodes():
        uf.make_set(node)

    # Trie les arêtes par poids croissant
    edges = g.get_edges()
    edges.sort(key=lambda e: e.get_weight())

    # Pour chaque arête
    for edge in edges:
        start = edge.get_start()
        end = edge.get_end()
        # Si la référence de start et de end sont différent
        # aka. ils n'appartienent pas au même ensemble
        if uf.find(start) != uf.find(end):
            # Ajoute cette arête à arbre. Il n'est pas orienté, on le fait aussi pour son transposé
            A.add_edge(edge)
            weight += edge.get_weight()
            # Union des 2 ensembles
            uf.union(start, end)
    return A, weight

# Algorithme de Prim
def prim(g, source):
	F = []
	trace = {}
	A = MST(g)
	weight = 0
	for node in g.get_nodes():
		cost = sys.maxsize
		if node == source:
			cost = 0
		trace[node] = [cost, None, node]
		heappush(F, trace[node])
	while len(F) != 0:
		curr = heappop(F)
		print "Curr = ", curr[-1]
		node_min = None
		for neighboor in [value[-1] for value in F if (curr[-1], value[-1]) in g.get_adj_matrix()]:
			min = sys.maxsize
			if trace[neighboor][0] > g.get_adj_matrix()[(curr[-1], neighboor)].get_weight():
				trace[neighboor][0] = g.get_adj_matrix()[(curr[-1], neighboor)].get_weight()
				trace[neighboor][1] = curr[-1]
				if trace[neighboor][0] < min:
					min = trace[neighboor][0]
					node_min = neighboor
		if node_min is None:
			node_min = curr[1]
		A.add_edge(g.get_adj_matrix()[(curr[-1], node_min)])
		weight += g.get_adj_matrix()[(curr[-1], node_min)].get_weight()

		F.sort()
		print '\n'
		print F, '\n'
	return A, weight


	# pour tout sommet t
	# 	cout[t] := +∞
	# 	pred[t] := nil
	# cout[s] := 0
	# F := file de priorité contenant les sommets de G avec cout[.] comme priorité
	# tant que F ≠ vide
	#     t := F.defiler
	#     pour toute arête t--u
	#         si cout[u] > poids(t--u)
	#                cout[u] := poids(t--u)
	#                pred[u] := t
	#                F.notifierDiminution(u)
	                
	# retourner pred