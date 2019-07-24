'''
1

The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to n (n ≤ 875714). Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks like : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.
'''

class Node:
    def __init__(self, value):
        self.vertex = value
        self.heads = []
        self.visited = False
        self.leader = None

    @staticmethod
    def addNode(g,edge):
        tail=g.get(edge[0],None)
        if tail is None:
            g[edge[0]]=Node(edge[0])
            tail=g.get(edge[0],None)
        head=g.get(edge[1],None)
        if head is None:
            g[edge[1]]=Node(edge[1])
            head=g.get(edge[1],None)
        tail.heads.append(head)
        return None
    
    @staticmethod
    def printStatus(g):
        for n_i in g.values():
            #print(n_i.vertex,n_i.visited,[i.vertex for i in n_i.heads])
            print(n_i,n_i.heads)
        return None
    
    @staticmethod
    def sscs(g):
        ssc={}
        for n_i in g.values():
            l_i=n_i.leader
            ssc_n=ssc.get(l_i,0)
            ssc[l_i]=ssc_n+1     
        return ssc
    


def dfs(graph,node,leader,t,f):
    nodeStack=[]
    nodeStack.append(node)
    #Node.printStatus(graph)
    

    while nodeStack:
        #print([i.vertex for i in nodeStack])
        node=nodeStack.pop(-1)
        node.visited=True
        f[-1].append(node.vertex)
        t[0]+=1
        node.leader = leader[0]
        
        for head_i in node.heads:
            if not head_i.visited:
                nodeStack.append(head_i)
                
    
    return None

def dfs2(graph,node,leader,t,f):
    if node.visited:
        return None
    node.visited=True
    node.leader=leader[0]
    for n_i in node.heads:
        if not n_i.visited:
            dfs2(graph,n_i,leader,t,f)
    t[0]+=1
    f.append(node.vertex)
    #print(t,node.vertex)

graph={}
graph_r={}
with open('SCC.txt', 'r') as f:
    for row in f:
        
        edge=[int(i) for i in row.split()]
        if len(edge)>0:
            Node.addNode(graph,edge)
            edge.reverse()
            Node.addNode(graph_r,edge)
import sys
sys.setrecursionlimit(1000000)
t=[0]
f=[]
leader=[None]
for v_i in graph_r.values():
    if not v_i.visited:
        
        leader[0]=v_i
        #Node.printStatus(graph)
        #print(v_i.vertex,'----------')
        f.append([])
        dfs(graph_r,v_i,leader,t,f)
[fi.reverse() for fi in f]
f2=[]
[f2.extend(fi) for fi in f] 

f2.reverse()
t=[0]
for f_i in f2:
    v_i=graph.get(f_i,None)
    if not v_i.visited:
        leader[0]=v_i
        #Node.printStatus(graph)
        #print(v_i.vertex,'----------')
        dfs(graph,v_i,leader,t,f)



print(sorted(Node.sscs(graph).values(),reverse=True)[:5])