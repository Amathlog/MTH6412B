# -*- coding: utf-8 -*-
import numpy as np
from math import cos, sin, pi


class Graph(object):
    """
    Une classe générique pour représenter un graphe comme un ensemble de
    noeuds.
    """

    def __init__(self, name='Sans nom', oriented=False):
        self.__name = name
        self.__nodes = []  # Attribut prive.
        self.__edges = []  # Attribut prive.
        self.__adjMatrix = None  # Attribut prive.
        self.__oriented = oriented  # Attribut prive.

    def add_node(self, node):
        "Ajoute un noeud au graphe."
        self.__nodes.append(node)

    def add_edge(self, edge):
        "Ajoute une arête au graphe."
        self.__edges.append(edge)
        self.__add_item_adj_matrix(edge)

    def get_name(self):
        "Donne le nom du graphe."
        return self.__name

    def get_nodes(self):
        "Donne la liste des noeuds du graphe."
        return self.__nodes

    def get_edges(self):
        "Donne la liste des arêtes du graphe."
        return self.__edges

    def get_adj_matrix(self):
        "Donne la matrice d'ajacence du graphe."
        return self.__adjMatrix

    def get_oriented(self):
        "Donne si le graphe est orienté."
        return self.__oriented

    def get_nb_nodes(self):
        "Donne le nombre de noeuds du graphe."
        return len(self.__nodes)

    def get_nb_edges(self):
        "Donne le nombre d'arêtes du graphe."
        return len(self.__edges)

    def __add_item_adj_matrix(self, edge):
        " Ajoute une arête dans la matrice d'adjacence"
        if self.__adjMatrix is None:
            self.__adjMatrix = np.zeros((self.get_nb_nodes(), self.get_nb_nodes()))

        start = edge.get_start().get_id() - 1
        end = edge.get_end().get_id() - 1
        self.__adjMatrix[start][end] = 1
        if not self.get_oriented():
            self.__adjMatrix[end][start] = 1

    def create_adj_matrix(self):
        "Crée la matrice d'adjacence lorsque le graphe est terminé"
        for edge in self.get_edges():
            self.__add_item_adj_matrix(edge)


    def plot_graph(self, connex=None, title=None):
        """
        Plot le graphe
        @param connex : Matrice d'ajacence de MÊME TAILLE que le graphe
                        Permet de rajouter une composante connexe sur le plot
                        Utile pour plot l'arbre de recouvrement donné par Kruskal
        @param title : Titre du plot, en string
        """

        import matplotlib.pyplot as plt
        from matplotlib.collections import LineCollection

        fig = plt.figure()
        ax = fig.add_subplot(111)
        if title is not None:
            fig.suptitle(title, fontsize=14, fontweight='bold')

        if self.get_nodes()[0].get_data() is not None:
            # Plot les noeuds.
            x = [node.get_data()[0] for node in self.get_nodes()]
            y = [node.get_data()[1] for node in self.get_nodes()]
        else:
            # S'il n'y a pas de coordonnées, crée le graphe en un polygone régulier
            rayon = 100
            x = [rayon * cos((node.get_id()) * 2 * pi / self.get_nb_nodes()) for node in self.get_nodes()]
            y = [rayon * sin((node.get_id()) * 2 * pi / self.get_nb_nodes()) for node in self.get_nodes()]

        # Plot les arêtes.
        edge_pos = np.asarray([((x[e.get_start().get_id()], y[e.get_start().get_id()]),
                                (x[e.get_end().get_id()], y[e.get_end().get_id()])) for e in self.get_edges()])
        edge_collection = LineCollection(edge_pos, linewidth=1.5, antialiased=True,
                                         colors=(.8, .8, .8), alpha=.75, zorder=0)
        ax.add_collection(edge_collection)
        ax.scatter(x, y, s=35, c='r', antialiased=True, alpha=.75, zorder=1)
        ax.set_xlim(min(x) - 10, max(x) + 10)
        ax.set_ylim(min(y) - 10, max(y) + 10)

        # Composante connexe en plus à tracer...
        if connex is not None:
            edge_pos_bis = np.asarray([((x[start], y[start]), (x[end], y[end]))
                                       for start in range(self.get_nb_nodes()) for end in range(self.get_nb_nodes())
                                       if connex[start][end] == 1])
            edge_collection_bis = LineCollection(edge_pos_bis, linewidth=1.5, antialiased=True,
                                             colors=(0, 0, 0), alpha=1, zorder=0)
            ax.add_collection(edge_collection_bis)

        plt.show()
        return

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
        G.add_edge(Edge(G.get_nodes()[k], G.get_nodes()[k + 1], 3))

    print G
