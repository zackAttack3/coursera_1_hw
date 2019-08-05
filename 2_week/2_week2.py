import math
import time
import queue as q



class Node():
    def __init__(self,val):
        self.vertex=val
        self.edges=set()
        self.visited=False
        self.distance=1000000
    def __lt__(self, other):
        return True

class Edge():
    def __init__(self,node1,node2,weight):
        self.weight=weight
        self.node2 = node2
        self.node1 = node1
        self.visited = False
    def __lt__(self, other):
        return True


graph={}
edges_={}
with open("dijkstraData.txt","r") as f:
    for row in f:
        row=row.rstrip().split('\t')
        if graph.get(int(row[0]),None) is None:
            graph[int(row[0])]=Node(int(row[0]))
        source=graph.get(int(row[0]),None)
        for edg_w in row[1:]:
            edge_i=edg_w.split(',')
            if graph.get(int(edge_i[0]),None) is None:
                graph[int(edge_i[0])]=Node(int(edge_i[0]))
            sink=graph.get(int(edge_i[0]),None)
            edge_key=','.join( [ str(i) for i in sorted([int(row[0]),int(edge_i[0])]) ] )
            if edges_.get(edge_key,None) is None:
                edges_[edge_key]=Edge(source,sink,int(edge_i[1]))
            edge_temp=edges_.get(edge_key,None)
            source.edges.add(edge_temp)
            sink.edges.add(edge_temp)

def not_optimum():
    start_time = time.time()
    node_i=graph[1]
    heap=list(node_i.edges)
    node_i.visited=True
    node_i.distance=0

    while heap:
        min_edge=1000000
        min_edge_i=None
        for counter,edge_i in enumerate(heap):
            if edge_i.node1.visited:
                source=edge_i.node1
                sink=edge_i.node2
            else:
                sink=edge_i.node1
                source=edge_i.node2
            if source.distance+edge_i.weight < sink.distance:
                sink.distance=source.distance+edge_i.weight

            if sink.distance <= min_edge:
                min_edge=sink.distance
                node_i=sink
                min_edge_i=counter
        heap.pop(min_edge_i).visited=True
        if not node_i.visited:         
            for edge_i in node_i.edges:
                if not edge_i.visited and not node_i.visited:
                    heap.append(edge_i)
        node_i.visited=True
        #print(source.vertex,node_i.vertex)
        
    ans=[]
    for i in [7,37,59,82,99,115,133,165,188,197]:
        ans.append(str(graph[i].distance))

    print(','.join(ans))

    print("--- %s seconds ---" % (time.time() - start_time))

#using heaps
not_optimum()
for j in graph.values():
    j.visited=False
for j in edges_.values():
    j.visited=False
heap_=[]
start_time = time.time()
node_i=graph[1]
node_i.distance=0
graph_len=len(graph)
while graph_len>1:
    if not node_i.visited:         
        for edge_i in node_i.edges:
            #print(edge_i.node1.vertex,edge_i.node2.vertex)
            if edge_i.visited:
                pass
            else:
                if edge_i.node1 == node_i:
                    sink=edge_i.node2
                else:
                    sink=edge_i.node1
                if node_i.distance+edge_i.weight < sink.distance:
                    sink.distance=node_i.distance+edge_i.weight
                q.heappush(heap_,(sink.distance,edge_i,sink))
    node_i.visited=True
    if not heap_:
            break
    vw,edge_i,sink=q.heappop(heap_)
    while sink.visited:
        if not heap_:
            break
        vw,edge_i,sink=q.heappop(heap_)
    #print(node_i.vertex,sink.vertex,vw,edge_i)
    edge_i.visited=True
    node_i=sink

ans=[]
for i in [7,37,59,82,99,115,133,165,188,197]:
    ans.append(str(graph[i].distance))

print(','.join(ans))

print("--- %s seconds ---" % (time.time() - start_time))


