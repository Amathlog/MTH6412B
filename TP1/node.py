# -*- coding: utf-8 -*-

class Node(object):
    """
    Une classe générique pour représenter les noeuds d'un graphe.
    """

    __node_count = -1   # Compteur global partage par toutes les instances.

    def __init__(self, name='Sans nom', data=None):
        self.__name = name
        self.__data = data
        Node.__node_count += 1
        self.__id = Node.__node_count

    def get_name(self):
        "Donne le nom du noeud."
        return self.__name

    def get_id(self):
        "Donne le numéro d'identification du noeud."
        return self.__id

    def get_data(self):
        "Donne les données contenues dans le noeud."
        return self.__data

    def __repr__(self):
        id = self.get_id()
        name = self.get_name()
        data = self.get_data()
        s  = 'Noeud %s (id %d)' % (name, id)
        #s += ' (donnees: ' + repr(data) + ')'
        return s

    def __eq__(self, other):
        return self.get_id() == other.get_id()

if __name__ == '__main__':

    nodes = []
    for k in range(5):
        nodes.append(Node())

    for node in nodes:
        print node
