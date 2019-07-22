import random as rdm
import copy

def help1(g,n1,n2):
    g[n1]=g[n1]+g[n2]
    #print(g)
    for ni in g.keys():
        for eni,ei in enumerate(g[ni]):
            if ei==n2:
                g[ni][eni]=n1
    #print(g)
    noloop=[]
    for eni,ei in enumerate(g[n1]):
        if ei==n1 or ei==n2:
            pass
        else:
            noloop.append(ei)
    g[n1]=list(noloop)
    #print(g)
    g.pop(n2,None)
    return None
def minCut(g):
    #return min cuts from graph
    while len(g)>2:
        n1i=rdm.randint(0,len(g)-1)
        n1=g.keys()[n1i]
        n2=g[n1][0]
        #print(n1,n2)
        #print(g)
        help1(g,n1,n2)
        #print(g)

    #print('---',g)
    
    return len(g[n1])
graph={}

with open('week4.txt', 'r') as f:
    for row in f:
        if row != '':
            
            x = [int(j) for j in row.strip().split('\t')] 
    
            if graph.get(x[0]) is None:
                graph[x[0]]=x[1:]
    
            else:
                graph[x[0]]+=x[1:]

ans = len(graph)*len(graph)
for i in range(len(graph)**2):
    ansn= minCut(copy.deepcopy(graph))
    #print(ansn)
    if ansn < ans:
        print(ansn)
        ans=ansn