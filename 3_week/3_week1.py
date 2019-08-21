import unittest
import heapq as hp
class Tests(unittest.TestCase):
    def setUp(self):
        self.alpha=Hw_()
        pass
    
    def test_1(self):
        self.assertEqual(1,2,self.alpha.schedule_())
    
    def test_2(self):
        self.assertEqual(-3612829.0,self.alpha.prism_al2(),'bad')
class Node:
    def __init__(self):
        self.visited=False
        self.vertex=None
class Edge:
    def __init__(self,n1,n2,w):
        self.nodes={n1,n2}
        self.weight=w
        self.visited=False
class Hw_:
    def __init__(self):
        self.ans1=None
        self.edges=[]
        self.edge_heap_map={}
    
    def schedule_(self):
        key_w_l=[]
        with open('jobs.txt') as f:
            f.readline()
            for row in f:
                if row.isspace():
                    continue
                w,l=[float(i) for i in row.split(' ')]
                key_w_l.append((w/l,w,l))
        key_w_l.sort(key=lambda x: (x[0],-x[1]),reverse=True)
        ans=0
        ci=0
        for w_l,w,l in key_w_l:
            ci+=l
            ans+=ci*w
        #print(key_w_l)
        return ans

    def prism_al(self):
        nodes=set()
        edges=set()
        with open("edges.txt") as f:
            f.readline()
            for row in f:
                if row.isspace():
                    continue
                n1,n2,w=[float(i) for i in row.split(' ')]
                nodes.update([n1,n2])
                edges.add(Edge(n1,n2,w))
        mine,minw=None,float("inf")
        span_tree={nodes.pop()}
        cost=0
        
        while nodes:
            for ei in edges:
                if ei.visited:
                    continue
                if ei.nodes.issubset(span_tree):
                    ei.visited=True
                    continue
                if len(ei.nodes.intersection(span_tree))==1 and ei.weight < minw:
                    mine,minw=ei,ei.weight
            mine.visited=True
            node2=mine.nodes.difference(span_tree).pop()
            #print(node2)
            nodes.discard(node2)
            span_tree.add(node2)
            cost+=mine.weight
            mine,minw=None,float("inf")
        print(cost)
        return cost
    def add_edge(self,w,n1,n2):
        entry=(1,w,set([n1,n2]))
        for ni in [n1,n2]:
            temp=self.edge_heap_map.get(ni,None)
            if temp is None:
                self.edge_heap_map[ni]=[entry]
            else:
                self.edge_heap_map[ni].append(entry)
        hp.heappush(self.edges,entry)


    def prism_al2(self):
        nodes=set()
        edges=[]
        with open("edges.txt") as f:
            f.readline()
            for row in f:
                if row.isspace():
                    continue
                n1,n2,w=[float(i) for i in row.split(' ')]
                nodes.update([n1,n2])
                self.add_edge(w,n1,n2)

        mine,minw=None,float("inf")
        
        cost=0
        span_tree=set()
        node_i = nodes.pop()
        span_tree.add(node_i)

        while nodes:
            
            for ei in self.edge_heap_map.get(node_i,None):
                if len(ei[2].difference(span_tree)) > 0:
                    hp.heappush(self.edges,(0,ei[1],ei[2]))
            min_edge=hp.heappop(self.edges)
            while len(min_edge[2].difference(span_tree)) != 1:
                #print(min_edge,min_edge[2].difference(span_tree))
                min_edge=hp.heappop(self.edges)
            node_i=min_edge[2].difference(span_tree).pop()
            span_tree.add(node_i)
            nodes.discard(node_i)
            cost+=min_edge[1]

        print(cost)
        return cost

if __name__ == "__main__":
    unittest.main()