# -*- coding: utf-8 -*-

class Edge(object):
    """
    Une classe generique pour representer une arête d'un graph.
    2 extrémités qui sont des noeuds et 1 poids.
    Les arêtes sont orientées, il y a un début et une fin.
    """

    def __init__(self, start, end, weight):
        if start == end and weight == 0:
            raise "Edge with same start and end and with a null weight : illegal"
        if not start or not end:
            raise "One of the extremity is equal to None"
        self.__start = start
        self.__end = end
        self.__weight = weight

    def get_start(self):
        "Donne le noeud de départ."
        return self.__start

    def get_end(self):
        "Donne le noeud de fin."
        return self.__end

    def get_weight(self):
        "Donne le poids de l'arête."
        return self.__weight

    def __repr__(self):
        return 'Arête ' + str(self.__start.get_id()) + '->' + str(self.__end.get_id()) + ' Poids=' + str(self.__weight)

if __name__ == '__main__':

    from node import Node

    nodes = []
    for k in range(3):
        nodes.append(Node('Hello' + str(k)))

    for node in nodes:
        print node

    edges = []
    for k in range(2):
        edges.append(Edge(nodes[k], nodes[k+1], 3))

    for edge in edges:
        print edge
