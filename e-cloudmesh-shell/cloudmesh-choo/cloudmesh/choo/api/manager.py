from cloudmesh.choo.switchyard.trains import Train
import time

class Manager(object):

    def __init__(self):
        print("init {name}".format(name=self.__class__.__name__))

    def list(self, parameter):
        print("list", parameter)

    def train_default(self):
        t = Train()
        print( t.default() )
        
    def train_move(self):
        t = Train()
        s = t.default()
        a = s.split('\n')
        l = len(a)
        m = 79
        for y in range(m, 0, -1):
            for x in range(0, l):
                print ( " "*y + a[x][:max(0,(len(a[x])-y))] + '\n')
            time.sleep(0.05)
