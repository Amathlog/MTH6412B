# -*- coding: utf-8 -*-

class NullExtremityEdge(Exception):
    """Classe exception dans le cas où une des extrémités
    d'une arête est égale à None"""
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
    """Classe exception dans le cas où on a une arête illégale"""
    def __str__(self):
        return "Edge with same start and end and with a null weight : illegal"
