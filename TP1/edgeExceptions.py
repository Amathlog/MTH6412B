

class NullExtremityEdge(Exception):
    def __init__(self, start=True):
        self.start = start

    def __str__(self):
        s = ''
        if self.start:
            s = 'Start'
        else:
            s = 'End'
        return s + ' is equal to None'


class IllegalEdge(Exception):
    def __str__(self):
        return "Edge with same start and end and with a null weight : illegal"
