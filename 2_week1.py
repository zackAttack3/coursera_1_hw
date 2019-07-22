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
        pass
    


def dfs(graph,node,leader,t,f):
    nodeStack=[]
    nodeStack.append(node)
    Node.printStatus(graph)
    node.leader = leader[0]

    while nodeStack:
        print([i.vertex for i in nodeStack])
        node=nodeStack.pop(-1)
        node.visited=True
        t[0]+=1
        f[t[0]]=node.vertex
        for head_i in node.heads:
            if not head_i.visited:
                nodeStack.append(head_i)
    
    return None


graph={}
graph_r={}
with open('SCC_2.txt', 'r') as f:
    for row in f:
        edge=[int(i) for i in row.split()]
        Node.addNode(graph,edge)
        edge.reverse()
        Node.addNode(graph_r,edge)

t=[0]
f={}
leader=[None]
for v_i in graph_r.values():
    if not v_i.visited:
        
        leader[0]=v_i
        Node.printStatus(graph)
        print(v_i.vertex,'----------')
        dfs(graph_r,v_i,leader,t,f)

for v_i in graph_r.values():
    #print(v_i.vertex,[i.vertex for i in v_i.heads])
    pass

print(f)