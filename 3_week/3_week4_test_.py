import unittest
import sys

class Test(unittest.TestCase):
    def setUp(self):
        sys.setrecursionlimit(3000)
        self.t1=knp1('knapsack1.txt')
        self.t2=knp1('knapsack2.txt')
    def test_1(self):
        self.assertEqual(0,1,self.t1.__init_a__())

    def test_2(self):
        self.assertEqual(0,1,self.t2.__init_b__())

class knp1:
    def __init__(self,name):
        self.ans=None 
        self.w_=0
        self.n_=0
        self.A_=[]
        self.nodes=[]
        self.cache={}
        
        with open(name) as f:
            self.w_,self.n_ = [int(i) for i in f.readline().rstrip().split(' ')]
            for row in f:
                self.nodes.append([int(i) for i in row.rstrip().split(' ')])
        

    def max_solv(self,n,w):
        if n==0 or w < 0 :
            return 0
        key1=str(n-1)+' '+str(w-1)
        key2=str(n-1)+' '+str(w-self.nodes[n-1][1])
        temp=[]
        if self.cache.get(key1,None) is None:
            self.cache[key1]=self.max_solv(n-1,w)
        temp.append(self.cache[key1])
        if w-self.nodes[n-1][1]>0 and self.cache.get(key2,None) is None:
            self.cache[key2]=self.max_solv(n-1,w-self.nodes[n-1][1])
        if w-self.nodes[n-1][1]>0:
            temp.append(self.cache[key2]+self.nodes[n-1][0])
        return max(temp)
    def __init_b__(self):
        return self.max_solv(self.n_,self.w_)
    def __init_a__(self):

        for i in range(0,self.n_):
            self.A_.append([None]*self.w_)
            for w in range(0,self.w_):
                if i==0:
                    self.A_[i][w]=0
                    continue
                temp=[self.A_[i-1][w]]
                if not self.nodes[i][1]>w:
                    temp.append(self.A_[i-1][w-self.nodes[i][1]]+self.nodes[i][0])
                self.A_[i][w] = max(temp)
        return self.A_[-1][-1]
                    


if __name__=="__main__":
    unittest.main(verbosity=3)
