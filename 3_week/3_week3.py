import unittest
import heapq

class Test(unittest.TestCase):
    def setUp(self):
        self.pr1=Hoffman()
        self.pr2=dinpro()

    def test_1(self):
        self.assertEqual((9,19),self.pr1.ans,'min_depth,max_depth')
    
    def test_2(self):
        self.assertEqual('10100110',self.pr2.ans,'dynamic programming')
        
class Node:
    def __init__(self,label,vx,prnt,lft,rgt):
        self.vertex=vx
        self.parent=prnt 
        self.left=lft 
        self.right=rgt
        self.visited=False
        self.label=label

class Hoffman:
    def __init__(self):
        self.hf=[]
        self.nlen=0
        self.ans=None

        with open('hoffman.txt') as f:
            self.nlen=int(f.readline().rstrip())
            for counter,row in enumerate(f):
                w=int(row.rstrip())
                self.hf.append( (w,Node(counter,w,None,None,None)) )

        heapq.heapify(self.hf)
        counter2=0

        while len(self.hf)>1:
            counter2+=1
            n1=heapq.heappop(self.hf)
            n2=heapq.heappop(self.hf)
            temp_n=Node(-1,n1[0]+n2[0],None,n1[1],n2[1])
            heapq.heappush(self.hf, ( n1[0]+n2[0], temp_n ) )


        root=self.hf[0][1]

        self.ans=self.min_depth(root)-1,self.max_depth(root)-1

    def max_depth(self,root):
        if root is None:
            return 0
        
        l_=self.max_depth(root.left)
        r_=self.max_depth(root.right)
        return max(l_,r_)+1

    def min_depth(self,root):
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.min_depth(root.right)+1
        if root.right is None:
            return self.min_depth(root.left)+1
        
        return min(self.min_depth(root.left),self.min_depth(root.right))+1
class dinpro:
    def __init__(self):
        self.n=0
        self.path=[]
        self.ind_set=set()
        self.qs=[1, 2, 3, 4, 17, 117, 517,997]
        self.ans=[0]*len(self.qs)
        
        with open('mwis.txt') as f:
            self.n=int(f.readline().rstrip())
            for row in f:
                self.path.append(int(row.rstrip()))
        #print(self.path)
        for i in range(2,len(self.path)):
            self.path[i] = max([ self.path[i-2]+self.path[i],self.path[i-1] ])
        #print(self.path)
        counter = len(self.path)-1
        while counter>0:
            if self.path[counter]==self.path[counter-1]:
                self.ind_set.add(counter-1+1)
                counter-=1
            else:
                self.ind_set.add(counter+1)
            counter-=2
        if counter == 0:
            self.ind_set.add(counter+1)
        #print(counter,self.ind_set)
        for i,val in enumerate(self.qs):
            if val in self.ind_set:
                self.ans[i]=1
        self.ans=''.join([str(i) for i in self.ans])

if __name__ == "__main__":
    unittest.main(verbosity=3)