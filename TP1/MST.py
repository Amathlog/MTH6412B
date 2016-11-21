from graph import Graph

class MST(Graph):

    def __init__(self, g):
        super(MST, self).__init__()
        self.__nodes = g.get_nodes()
        self.__oriented = g.get_oriented()
        self.__weight = 0

    def get_weight(self):
        return self.__weight

    def add_edge(self, edge):
        super(MST, self).add_edge(edge)
        self.__weight += edge.get_weight()
