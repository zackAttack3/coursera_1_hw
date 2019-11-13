import unittest
import math
import datetime
import itertools

class TSP:
    def __init__(self,file,S):
        self.n=0
        self.nodes=[]
        self.adj=[]
        self.memo=[]
        self.S=S
        with open (file) as f:
            self.n=int(f.readline())
            for row in f:
                self.nodes.append([float(i) for i in row.rstrip().split(' ')])
        
        for i in range(self.n):
            self.adj.append([])
            for j in range(self.n):
                self.adj[i].append(self._eucl_dist(i,j))
        
        for i in range(self.n):
            self.memo.append([])
            for j in range(2**self.n):
                self.memo[i].append(math.inf)
    def setUp(self):
        for i in range (self.n):
            if i==self.S:
                continue
            #print(i,1<<self.S | 1 <<i,self.adj[self.S][i])
            self.memo[i][1<<self.S | 1 <<i]=self.adj[self.S][i]
        
    def solve(self):
        powers=[1<<i for i in range(self.n)]
        for r in range(3,self.n+1):
            print(r)
            for subset in itertools.combinations(powers,r):
                if self.__not_in(self.S,sum(subset)): 
                    continue
                for next_ in range(0,self.n):
                    if next_==self.S or self.__not_in(next_,sum(subset)):
                        continue
                    state = sum(subset) ^ (1<<next_)
                    minDist = math.inf

                    for e in range(0,self.n):
                        if e==self.S or e==next_ or self.__not_in(e,sum(subset)):
                            continue
                        newDist = self.memo[e][state]+self.adj[e][next_]
                        #print(newDist,minDist)
                        if newDist < minDist:
                            minDist=newDist
                    self.memo[next_][sum(subset)] = minDist
                #print(self.memo)
    def findminCost(self):
        end_state = (1<<self.n) -1
        mintour = math.inf
        for e in range(self.n):
            if e == self.S: continue
            tourCost = self.memo[e][end_state] + self.adj[e][self.S]
            if tourCost < mintour:
                mintour =  tourCost
        return mintour


    def __not_in(self,i,subset):
        return (1<<i & subset) == 0
    
    def comb_bit(self,r):
        subsets=set()
        self.comb_bit2(0,0,r,subsets)
        return subsets
    def comb_bit2(self,set_,at_,r,subsets_):
        if r==0:
            subsets_.add(set_)
        else:
            for i in range(at_,self.n):
                set_ = set_ or (1<<i)
                self.comb_bit2(set_,i+1,r-1,subsets_)
                set_ = set_ and ~(1<<i)

    def _eucl_dist(self,x,y):
        return ((self.nodes[x][0]-self.nodes[y][0])**2+(self.nodes[x][1]-self.nodes[y][1])**2)**0.5
    
class Test(unittest.TestCase):
    def setUp(self):
        self.prob1=TSP('tsp2.txt',0)
        print(datetime.datetime.now())
        self.prob1.setUp()
        print(datetime.datetime.now())
        self.prob1.solve()
        print(datetime.datetime.now())
        self.prob1.findminCost()
        print(datetime.datetime.now())
        print(self.prob1.findminCost())
        print(14409+14662-2*self.prob1._eucl_dist(11,12))
    def test_1(self):
        pass

if __name__ == "__main__":
    unittest.main(verbosity=4)