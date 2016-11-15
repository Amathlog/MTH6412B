from graph import Graph

class MST(Graph):

    def __init__(self, g):
        super(MST, self).__init__()
        self.__nodes = g.get_nodes()
        self.__oriented = g.get_oriented()
