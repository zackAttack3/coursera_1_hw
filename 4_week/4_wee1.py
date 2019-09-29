import unittest
import math
import heapq

class Graps:
    def __init__(self):
        self.nodes=0
        self.edges=[]
    def load_file(self,file):
        
        with open (file) as f:
            temp = [int(i) for i in f.readline().rstrip().split(' ')]
            self.nodes=temp[0]
            for row in f:
                self.edges.append([int(i) for i in row.rstrip().split(' ')])

class BellmanF(Graps):
    def __init__(self):
        super().__init__()
        self.A=None
    def is_neg_cycle(self):
        self.short_path(0)
        return not all(self.A[-1][x]==self.A[-2][x] for x in range(self.nodes))

    def short_path(self,source):
        self.A=list()
        self.A.append(list([math.inf]*self.nodes))
        self.A[0][source]=0
        i=1
        for i in range(1,self.nodes+1):
            self.A.append(list([math.inf]*self.nodes))
            for t,h,w in self.edges:
                temp=min(self.A[i][h-1],self.A[i-1][h-1],self.A[i-1][t-1]+w)
                self.A[i][h-1]=min(self.A[i][h-1],self.A[i-1][h-1],self.A[i-1][t-1]+w)
        return 1

class Johnson(BellmanF):
    def __init__(self):
        super().__init__()
        self.n2=0
        self.edges2=None
        self.short_paths_all=None
    def djksta(self,source):
        graph={}
        for t,h,w in self.edges:
            t-=1
            h-=1
            if graph.get(t,None) is None:
                graph[t]={h:w}
            else:
                if graph[t].get(h,None) is None:
                    graph[t][h]=w
        #print(graph)
        A_d= [math.inf]*self.nodes
        queue=list()
        heapq.heapify(queue)
        heapq.heappush(queue,[0,source])
        while queue:
            path_l, v = heapq.heappop(queue)
            if math.isinf(A_d[v]):
                A_d[v] = path_l
                if graph.get(v,None) is None:
                    continue
                for w,edge_len in graph[v].items():
                    if math.isinf(A_d[w]):
                        heapq.heappush(queue,[path_l+edge_len,w])
        for i in range(self.nodes):
            A_d[i] +=( 0 - self.A[-1][source]+self.A[-1][i])
        
        return A_d

    def a_short_paths(self):

        self.n2=self.nodes
        self.edges2=list(self.edges)
        self.nodes=self.nodes+1
        
        for i in range(1,self.nodes):
            self.edges.append([self.nodes,i,0])
        
        self.short_path(self.nodes-1)
        print(not all(self.A[-1][x]==self.A[-2][x] for x in range(self.nodes)))
        print(min(self.A[-1]))
        
        for i,[t,h,w] in enumerate(self.edges2):
            self.edges2[i][2]+=(self.A[-1][t-1]-self.A[-1][h-1])
        self.edges=list(self.edges2)
        self.nodes=self.n2

        self.short_paths_all=[math.inf]*self.nodes
        for i in range(self.nodes):

            self.short_paths_all[i] = min(self.djksta(i))
        print(self.short_paths_all)
        print(min(self.short_paths_all))
        return 1
        


class Test(unittest.TestCase):
    def setUp(self):
        #self.g1=BellmanF()
        #self.g2=BellmanF()
        self.g3=Johnson()
        #self.g1.load_file('g1.txt')
        #self.g2.load_file('g2.txt')
        self.g3.load_file('g3.txt')
        
    def test_1(self):
        self.assertEqual(1,0,None)
    def test_2(self):
        #self.assertTrue(self.g1.is_neg_cycle())
        pass
    def test_3(self):
        #self.assertTrue(self.g2.is_neg_cycle())
        pass
    def test_4(self):
        #self.assertTrue(self.g3.is_neg_cycle())
        self.g3.a_short_paths()

if __name__ == "__main__":
    unittest.main(verbosity=4)