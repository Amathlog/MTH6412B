# -*- coding: utf-8 -*-

from edgeExceptions import NullExtremityEdge, IllegalEdge

class Edge(object):
    """
    Une classe generique pour representer une arête d'un graph.
    2 extrémités qui sont des noeuds et 1 poids.
    Les arêtes sont orientées, il y a un début et une fin.
    """

    def __init__(self, start, end, weight):
        # Gestion des cas particuliers.
        if start == end and weight == 0:
            raise IllegalEdge()
        if not start:
            raise NullExtremityEdge(start=True)
        if not end:
            raise NullExtremityEdge(start=False)

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
        return 'Arête ' + str(self.get_start().get_id()) + '->' + \
               str(self.get_end().get_id()) + ' Poids=' + str(self.get_weight())

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

    # ---------------------------------------------
    #  Test des cas particuliers
    catched = False

    def checkCatched(bool):
        if bool:
            print 'OK'
        else:
            print 'FAILED'

    print '\n---------------'
    try:
        print "Test start = None :",
        aux = Edge(None, nodes[0], 3)
    except NullExtremityEdge as e:
        catched = (e.start == True)
    except Exception as e:
        catched = False

    checkCatched(catched)
    catched = False

    try:
        print "Test end = None :",
        aux = Edge(nodes[0], None, 3)
    except NullExtremityEdge as e:
        catched = (e.start == False)
    except Exception as e:
        catched = False

    checkCatched(catched)
    catched = False

    try:
        print "Test start = end et weight = 0 :",
        aux = Edge(nodes[0], nodes[0], 0)
    except IllegalEdge as e:
        catched = True
    except Exception as e:
        catched = False

    checkCatched(catched)
