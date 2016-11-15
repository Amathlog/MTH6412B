# -*- coding: utf-8 -*-

import numpy as np
import sys
from priorityQueue import PriorityQueue
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
    # File de priorité
    priorityQ = PriorityQueue()
    # Garde trace des parents pour chaque noeud
    ancestors = {}
    # Arbre de poids minimum
    A = MST(g)
    # Poids de l'arbre minimum
    weight = 0
    # Initialisation pour tous les noeuds
    for node in g.get_nodes():
        # côut inital = +∞
        # coût source = 0
        cost = sys.maxsize
        if node == source:
        	cost = 0
        # parent initial = None
        ancestors[node] = None
        # On pousse dans la file de priorité
        priorityQ.enqueue(node, cost)
    # Tant que le heap n'est pas vide (ie. il reste des sommets à joindre)
    while len(priorityQ) != 0:
        # On récupère celui avec la priorité la plus faible
        curr = priorityQ.dequeue()
        # On récupère la liste de ses voisins qu'ils restent encore à connecter (ie. qui sont encore dans la file)
        for neighboor in [value for value in priorityQ.get_list_items() if (curr, value) in g.get_adj_matrix()]:
            # Si le coût de ce noeud est plus élevé que le coût de l'arc
            if(priorityQ.get_priority(neighboor) > g.get_adj_matrix()[(curr, neighboor)].get_weight()):
                # On change le coût dans la file de ce noeud
                priorityQ.change_priority(neighboor, g.get_adj_matrix()[(curr, neighboor)].get_weight())
                # Curr devient le nouveau parent de neighboor
                ancestors[neighboor] = curr

    # Lorsqu'on a la liste de tous les parents, on crée le graphe à partir de g
    for node in g.get_nodes():
        # Seul le noeud source n'a pas de parent
        if node == source:
            continue
        A.add_edge(g.get_adj_matrix()[(node, ancestors[node])])
        weight += g.get_adj_matrix()[(node, ancestors[node])].get_weight()

    return A, weight