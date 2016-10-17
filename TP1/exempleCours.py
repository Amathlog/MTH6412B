# -*- coding: utf-8 -*-

""" Hard code l'exemple du cours pour tester l'algorithme de Kruskal """

from graph import Graph
from node import Node
from edge import Edge
from kruskal import kruskal

g = Graph('Exemple Cours')

nodes = [(0, 2),
         (2, 4),
         (4, 4),
         (6, 4),
         (8, 2),
         (6, 0),
         (4, 0),
         (2, 0),
         (3, 2)]

edges = [(0, 1, 4),
         (1, 2, 8),
         (2, 3, 7),
         (3, 4, 9),
         (4, 5, 10),
         (5, 6, 2),
         (6, 7, 1),
         (7, 0, 8),
         (1, 7, 11),
         (7, 8, 7),
         (8, 2, 2),
         (8, 6, 6),
         (2, 5, 4),
         (3, 5, 14)]

for d in nodes:
    g.add_node(Node(data=d))

for e in edges:
    g.add_edge(Edge(g.get_nodes()[e[0]], g.get_nodes()[e[1]], e[2]))

g.create_adj_matrix()

# print g
# print g.get_adj_matrix()

connex, weight = kruskal(g)

g.plot_graph(connex=connex, title='Poids minimum : ' + str(weight))
