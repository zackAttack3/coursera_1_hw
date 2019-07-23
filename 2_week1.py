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
        t[0]+=1
        node.leader = leader[0]
        
        for head_i in node.heads:
            if not head_i.visited:
                nodeStack.append(head_i)
        if nodeStack:
            f.append(nodeStack[-1].vertex)
    
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
        dfs2(graph_r,v_i,leader,t,f)
print(f[:5])
f.reverse()
t=[0]
for f_i in f:
    v_i=graph.get(f_i,None)
    if not v_i.visited:
        leader[0]=v_i
        #Node.printStatus(graph)
        #print(v_i.vertex,'----------')
        dfs2(graph,v_i,leader,t,f)



print(sorted(Node.sscs(graph).values(),reverse=True)[:5])