# -*- coding: utf-8 -*-


class UnionFind(object):
    def __init__(self):
        self.__parent = dict()
        self.__rang = dict()

    def make_set(self, item):
        self.__parent[item] = item
        self.__rang[item] = 0

    def find(self, item):
        """ Compression des chemins. Le parent de chaque noeud de l'arbre
        est la racine de l'arbre"""
        if self.__parent[item] != item:
            self.__parent[item] = self.find(self.__parent[item])
        return self.__parent[item]

    def union(self, item1, item2):
        root1 = self.find(item1)
        root2 = self.find(item2)

        if self.__rang[root1] < self.__rang[root2]:
            self.__parent[root2] = self.__parent[root1]
        elif self.__rang[root1] > self.__rang[root2]:
            self.__parent[root1] = self.__parent[root2]
        else:
            self.__parent[root2] = self.__parent[root1]
            self.__rang[root1] += 1
