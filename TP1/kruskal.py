# -*- coding: utf-8 -*-

import numpy as np

# Structure de Union-Find
# https://fr.wikipedia.org/wiki/Union-Find

parent = dict()


def make_set(item):
    parent[item] = item


def find(item):
    if parent[item] != item:
        parent[item] = find(parent[item])
    return parent[item]


def union(item1, item2):
    root1 = find(item1)
    root2 = find(item2)
    if root1 != root2:
        parent[root1] = parent[root2]


# Algorithme de Kruskal
def kruskal(g):
    # Initialise le poids total à 0
    weight = 0

    # Initialise la matrice d'adjacence à une matrice carré de taille le nombre de noeuds du graphe remplie de 0
    A = np.zeros((g.get_nb_nodes(), g.get_nb_nodes()))

    # Crée un ensemble singleton pour chaque sommet
    for node in g.get_nodes():
        make_set(node)

    # Trie les arêtes par poids croissant
    edges = g.get_edges()
    edges.sort(key=lambda e: e.get_weight())

    # Pour chaque arête
    for edge in edges:
        start = edge.get_start()
        end = edge.get_end()
        # Si la référence de start et de end sont différent
        # aka. ils n'appartienent pas au même ensemble
        if find(start) != find(end):
            # Ajoute cette arête à notre matrice. Il n'est pas orienté, on le fait aussi pour son transposé
            A[start.get_id()][end.get_id()] = 1
            A[end.get_id()][start.get_id()] = 1
            weight += edge.get_weight()
            # Union des 2 ensembles
            union(start, end)
    return A, weight
