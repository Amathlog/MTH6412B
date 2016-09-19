# -*- coding: utf-8 -*-

class Graph(object):
    """
    Une classe générique pour représenter un graphe comme un ensemble de
    noeuds.
    """

    def __init__(self, name='Sans nom'):
        self.__name = name
        self.__nodes = []   # Attribut prive.
        self.__edges = []   # Attribut prive.

    def add_node(self, node):
        "Ajoute un noeud au graphe."
        self.__nodes.append(node)

    def add_edge(self, edge):
        "Ajoute une arête au graphe."
        self.__edges.append(edge)

    def get_name(self):
        "Donne le nom du graphe."
        return self.__name

    def get_nodes(self):
        "Donne la liste des noeuds du graphe."
        return self.__nodes

    def get_edges(self):
        "Donne la liste des arêtes du graphe."
        return self.__edges

    def get_nb_nodes(self):
        "Donne le nombre de noeuds du graphe."
        return len(self.__nodes)

    def get_nb_edges(self):
        "Donne le nombre d'arêtes du graphe."
        return len(self.__edges)

    def __repr__(self):
        name = self.get_name()
        nb_nodes = self.get_nb_nodes()
        s = 'Graphe %s comprenant %d noeuds' % (name, nb_nodes)
        for node in self.get_nodes():
            s += '\n  ' + repr(node)
        s += '\n\n'
        s += 'Avec ' + str(self.get_nb_edges()) + ' arête' + ('s' if self.get_nb_edges() > 1 else '') + ' :'
        for edge in self.get_edges():
            s += '\n  ' + repr(edge)
        return s


if __name__ == '__main__':

    from node import Node
    from edge import Edge

    G = Graph(name='Graphe test')
    for k in range(5):
        G.add_node(Node(name='Noeud test %d' % k))

    for k in range(2):
        G.add_edge(Edge(G.get_nodes()[k], G.get_nodes()[k+1], 3))

    print G
