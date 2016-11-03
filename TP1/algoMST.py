# -*- coding: utf-8 -*-

import numpy as np
from unionFind import UnionFind

# Algorithme de Kruskal
def kruskal(g):
    # Initialise le poids total à 0
    weight = 0

    # Initialise la structure d'Union Find
    uf = UnionFind()

    # Initialise la matrice d'adjacence à une matrice carré de taille le nombre de noeuds du graphe remplie de 0
    A = np.zeros((g.get_nb_nodes(), g.get_nb_nodes()))

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
            # Ajoute cette arête à notre matrice. Il n'est pas orienté, on le fait aussi pour son transposé
            A[start.get_id()][end.get_id()] = 1
            A[end.get_id()][start.get_id()] = 1
            weight += edge.get_weight()
            # Union des 2 ensembles
            uf.union(start, end)
    return A, weight

# Algorithme de Prim
def prim(g):
    return
