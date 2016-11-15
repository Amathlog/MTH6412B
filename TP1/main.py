# -*- coding: utf-8 -*-

""" Argument 1 : Nom du fichier stsp à parser et utiliser
    Argument 2 : 0 = Kruskal 
                 1 = Prim (défaut)
"""

import read_stsp
from graph import Graph
from node import Node
from edge import Edge
from algoMST import kruskal, prim

import sys

finstance = sys.argv[1]

kruskal_activated = False
if len(sys.argv) > 2:
   kruskal_activated = (sys.argv[2] == "0")

with open(finstance, "r") as fd:

    header = read_stsp.read_header(fd)
    print 'Header: ', header
    dim = header['DIMENSION']
    edge_weight_format = header['EDGE_WEIGHT_FORMAT']

    print "Reading nodes"
    nodes = read_stsp.read_nodes(header, fd)

    print "Reading edges"
    edges = read_stsp.read_edges(header, fd)
    edge_list = []
    for k in range(dim):
        edge_list.append([])
    for e in edges:
        if edge_weight_format in ['UPPER_ROW', 'LOWER_COL', \
                'UPPER_DIAG_ROW', 'LOWER_DIAG_COL']:
            edge_list[e[0]].append((e[1], int(e[2])))
        else:
            edge_list[e[1]].append((e[0], int(e[2])))
    for k in range(dim):
        edge_list[k].sort()

    g = Graph(header['NAME'])

    if not nodes:
        for i in range(dim):
            g.add_node(Node(str(i)))
    else:
        for i in range(dim):
            g.add_node(Node(str(i), nodes[i]))

    for i in range(dim):
        for pair in edge_list[i]:
            if i == pair[0] and pair[1] == 0:
                continue
            g.add_edge(Edge(g.get_nodes()[i], g.get_nodes()[pair[0]], pair[1]))

    #g.create_adj_matrix()

    # print g
    # print g.get_adj_matrix()

    if kruskal_activated:
        mst, weight = kruskal(g)
        text = " (kruskal)"
    else:
        mst, weight = prim(g, g.get_nodes()[0])
        text = " (prim)"

    g.plot_graph(mst=mst, title='Poids minimum : ' + str(weight) + text)

