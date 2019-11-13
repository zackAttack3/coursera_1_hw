import unittest
import heapq
import datetime
import math
class Test(unittest.TestCase):
    def setUp(self):
        self.prob1=TSP('nn.txt')
        self.prob1.solve()
    def test_1(self):
        self.assertEqual(1,0,self.prob1.total_dist)

class TSP:
    def __init__(self,file):
        self.n=0
        self.x_y=[]
        self.dist=[]
        self.visited=set()
        self.total_dist=0
        with open(file) as f:
            self.n=int(f.readline().rstrip())
            for row in f:
                self.x_y.append([float(i) for i in row.rstrip().split(' ')])
        for i in range(self.n):
            self.visited.add(i)
        
    def solve(self):
        vx=0
        
        self.visited.remove(vx)
        temp=len(self.visited)
        print(temp,datetime.datetime.now())
        while self.visited:
            heap=[]
            for i in self.visited:
                heapq.heappush(heap,(self.eucl(vx,i),i))
            if len(self.visited)==temp:
                print(temp,datetime.datetime.now())
                temp=max([0,temp-1000])
            dist,vx=heapq.heappop(heap)
            self.total_dist+=math.sqrt(dist)
            self.visited.remove(vx)
        self.total_dist+=math.sqrt(self.eucl(vx,0))
    
    def eucl(self,n1,n2):
        return (self.x_y[n1][1]-self.x_y[n2][1])**2+(self.x_y[n1][2]-self.x_y[n2][2])**2
if __name__ == "__main__":
    unittest.main(verbosity=4)