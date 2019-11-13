import unittest
import random
import math
import datetime
from itertools import chain
from collections import defaultdict

class _2sat:
    def __init__(self,file_):
        self.n=0
        self.clauses=[]
        self.vars=None
        self.cannot_del=set()

        with open(file_) as f:
            self.n = int(f.readline())
            for row in f:
                temp=[int(i) for i in row.rstrip().split(' ')]
                self.clauses.append(temp)
        
        self.init_guess()
        
    
    def init_guess(self):
        temp=1<<self.n
        #print(temp)
        for i in self.cannot_del:
            if i<0: i=-1*i
            if random.randint(0,1):
                #print('-',temp,1<<i)
                temp=temp ^ (1 << i)
                #print(temp)
        self.vars=temp

    def reduce_(self):
        nodes_p=set()
        nodes_n=set()
        for temp in self.clauses:
            for ci in temp:
                if ci>0:
                    nodes_p.add(ci)
                else:
                    nodes_n.add(-ci)

        cannot_del=nodes_p.intersection(nodes_n)
        cannot_del.update([-i for i in cannot_del])
        
        new_clauses=list()
        for ni in self.clauses:
            if set(ni) == set(ni).intersection(cannot_del):
                new_clauses.append(ni)
        before= len(self.clauses)

        self.clauses=list(new_clauses)
        self.cannot_del=set(cannot_del)
        return before==len(self.clauses) 
        
    
    def check_(self):
        cl2=set([i for i in range( len(self.clauses) )])
        cl_f=set()
        #print(self.vars)
        while cl2:
            temp1=cl2.pop()
            mi=[]
            for ni in self.clauses[temp1]:
                if ni >= 0:
                    mi.append(self.vars & (1 << abs(ni)) > 0 )
                else:
                    mi.append(self.vars & (1 << abs(ni)) == 0 )
            #print(mi)
            if mi[0] | mi[1]:
                pass
            else:
                cl_f.add(temp1)
                #return cl_f
        #print(len(cl_f),self.n,len(self.redux))
        return cl_f

    
    def neighbor_(self):

        while not self.reduce_():
            continue
        print('-',len(self.clauses))
        
        for _ in range(int(math.log2(self.n))*5 ):
            self.init_guess()
            
            print(datetime.datetime.now())
            
            for _ in range (10000):
                #print(self.vars)
                cl_f=self.check_()
                if not cl_f:
                    #print('hey',cl_f)
                    return 1 
                else:
                    temp1=cl_f.pop()
                    while random.randint(0,5) in set([1]) and cl_f:
                        temp1=cl_f.pop()
                    ni=list(self.clauses[temp1])
                    self.vars=self.vars ^ (1 << abs(ni[random.randint(0,1)]))
                
        return 0

class Test(unittest.TestCase):
    def setUp(self):
        pass
    def load_file(self,i):
        self.p= _2sat('/Users/sw/Desktop/coursera/hw/4_week/2sat{0}.txt'.format(i)) 
        
    def test_1(self):
        for i in range(1,7):
            with self.subTest(i):
                self.load_file(i)
                self.assertEqual(1,self.p.neighbor_(),i)

if __name__ == "__main__":
    unittest.main(verbosity=4)