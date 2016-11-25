# -*- coding: utf-8 -*-

import read_stsp
from graph import Graph
from node import Node
from edge import Edge
from algoMST import kruskal, prim
from TSPSolve import solveTSP

import sys



# Récupération de la liste de tous les fichiers stsp
TSPpath = "./instances/stsp/"

from os import listdir
from os.path import isfile, join
files = [f for f in listdir(TSPpath) if isfile(join(TSPpath, f))]

# Récupération des valeurs des chemins optimaux
best_ones = {}
with open("./res/bestones.txt") as fd:
    for line in fd:
        aux = line.split()
        best_ones[aux[0]] = int(aux[2])

# Boucle sur tous les fichiers
for file in files:

    with open(TSPpath + file, "r") as fd:

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

        min = 2*[sys.maxsize]
        travel = [None, None]
        for i in range(2):
            for node in g.get_nodes():
                aux = solveTSP(g, node, i==0)
                if(aux.get_weight() < min):
                    travel[i] = aux
                    min[i] = aux.get_weight()

        filename = file.split('.')[0]
        optimal = best_ones[filename]
        
        g.plot_graph(mst=travel[0], title='Prim: ' + str(travel[0].get_weight()) + " ; Optimal: " + str(optimal) + " (Error: " + str(travel[0].get_weight() - optimal) + ")", show=False, filename="./res/"+filename+"_prim")
        g.plot_graph(mst=travel[1], title='Kruskal: ' + str(travel[1].get_weight()) + " ; Optimal: " + str(optimal) + " (Error: " + str(travel[1].get_weight() - optimal) + ")", show=False, filename="./res/"+filename+"_kruskal")