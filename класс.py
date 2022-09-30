from sys import stdin
from copy import deepcopy


class Matrix(object):
    def __init__(self, mylist):
        self.myListCopy = deepcopy(mylist)

    def __str__(self):
        mystr = str()
        for i in self.myListCopy:
            mystrtab = '\t'.join(map(str, i)) + '\n'
            mystr = str(mystr + mystrtab)
        return mystr[:-1]

    def size(self):
        s = (len(self.myListCopy), len(self.myListCopy[0]))
        return s


exec(stdin.read())
