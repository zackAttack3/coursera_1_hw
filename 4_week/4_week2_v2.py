import math
import itertools
class TSP:
    def __init__(self,file,S):
        self.n=0
        self.nodes=[]
        self.adj=[]
        self.memo=[]
        self.S=S
        with open (file) as f:
            self.n=int(f.readline())
            for row in f:
                self.nodes.append([float(i) for i in row.rstrip().split(' ')])
        
        for i in range(self.n):
            self.adj.append([])
            for j in range(self.n):
                self.adj[i].append(self._eucl_dist(i,j))
        
        for i in range(self.n*0):
            self.memo.append([])
            for j in range(2**self.n):
                self.memo[i].append(math.inf)
    def _eucl_dist(self,x,y):
        return ((self.nodes[x][0]-self.nodes[y][0])**2+(self.nodes[x][1]-self.nodes[y][1])**2)**0.5

def length(x, y):
    dx = x[0] - y[0]
    dy = x[1] - y[1]
    return math.sqrt(dx*dx + dy*dy)

def solve_tsp_dynamic(points):
    #calc all lengths
    all_distances = [[length(x,y) for y in points] for x in points]
    #initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
    cnt = len(points)
    for m in range(2, cnt):
        print(m)
        #B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                A[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
        #A = B
    #print(A)
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    #print A
    return res[0]
    
def main():
    # points = [[20833.3333, 17100.0000],
#                 [20900.0000, 17066.6667],
#                 [21300.0000, 13016.6667],
#                 [21600.0000, 14150.0000],
#                 [21600.0000, 14966.6667],
#                 [21600.0000, 16500.0000],
#                 [22183.3333, 13133.3333],
#                 [22583.3333, 14300.0000],
#                 [22683.3333, 12716.6667],
#                 [23616.6667, 15866.6667],
#                 [23700.0000, 15933.3333],
#                 [23883.3333, 14533.3333],
#                 [24166.6667, 13250.0000],
#                 [25149.1667, 12365.8333],
#                 [26133.3333, 14500.0000],
#                 [26150.0000, 10550.0000],
#                 [26283.3333, 12766.6667],
#                 [26433.3333, 13433.3333],
#                 [26550.0000, 13850.0000],
#                 [26733.3333, 11683.3333],
#                 [27026.1111, 13051.9444],
#                 [27096.1111, 13415.8333],
#                 [27153.6111, 13203.3333],
#                 [27166.6667, 9833.3333],
#                 [27233.3333, 10450.0000]]
    points = [[2, 5],
              [7, 5],
              [2, 1],
              [7, 1]]
    print(solve_tsp_dynamic(points))

    prob1=TSP('tsp2.txt',0)
    print(solve_tsp_dynamic(prob1.adj))

    print(210.82+3717.23-2*length(prob1.adj[11],prob1.adj[12]))
    
if __name__ == "__main__":
    main()