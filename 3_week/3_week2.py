import unittest
from unionfind import UnionFind
import itertools as it

class Test(unittest.TestCase):
    def setUp(self):
        self.ans1=Clustering()
        self.ans2=Clustering2()
        pass

    def test_1(self):
        self.assertEqual(0,self.ans1.cluster1(),'None')

    def test_2 (self):
        self.assertEqual(0,1,'test2')

class Clustering2:
    def __init__(self):
        self.alpha={}
        self.input=None
        nodei=0
        with open ('clustering.txt') as f:
            self.input=[int(i) for i in f.readline().rstrip().split(' ')]
            for row in f:
                if row.isspace():
                    continue
                hammi=int(row.rstrip().replace(' ',''),2)
                if self.alpha.get(hammi,None) is None:
                    self.alpha[hammi]=set([nodei])
                else:
                    self.alpha[hammi].add(nodei)
                nodei+=1
        
        uf=UnionFind([i for i in range(self.input[0])])
        masks=[0]
        mask_1=[1 << i for i in range(self.input[1])]
        for i in it.combinations(mask_1,2):
            masks.append(i[0] ^ i[1])
        masks.extend(mask_1)

        for key in self.alpha:
            for di in masks:
                if self.alpha.get(di ^ key,None) is not None:
                    temp_=self.alpha[key].union(self.alpha[di^key])
                    leader=temp_.pop()
                    for tempi in temp_:
                        uf.union(leader,tempi)
        print(uf.n_comps,uf.n_elts)
        
class Clustering:
    def __init__(self):
        self.edges=[]
        self.clusters=[0]*501
        
        with open('clustering1.txt') as f:
            self.k=int(f.readline())
            for row in f:
                if row.isspace():
                    continue
                n1,n2,w=[int(i) for i in row.rstrip().split(' ')]
                for ni in [n1,n2]:
                    self.clusters[ni]=ni
                self.edges.append([w,n1,n2])
    def cluster1_(self,n1,n2):
        #print(self.clusters)
        old=self.clusters[n1]
        for i,key in enumerate(self.clusters):
            
            if self.clusters[i] == old:
                #print('o',i,key,self.clusters[n1])
                self.clusters[i]=self.clusters[n2]
        #print(self.clusters)
    def cluster1(self):
        self.edges.sort()
        print(self.k)

        for w,n1,n2 in self.edges:

            if self.k<=4 and self.clusters[n1] != self.clusters[n2]:
                print('ans',w,n1,n2)
                break
            if self.k>4 and self.clusters[n1] != self.clusters[n2]:
                self.cluster1_(n1,n2)
                #print(w,n1,n2)
                self.k-=1
            else:
                pass
                
        #print(self.k,self.clusters)

        return None

if __name__=="__main__":
    unittest.main()