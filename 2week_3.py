'''

The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 5 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, the kth median mk is defined as the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)
In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you should compute (m1+m2+m3+⋯+m10000)mod10000.
OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.

'''

class Heap_:
    def __init__(self):
        self.heap=[]
        self.n=0
    
    def add_node(self,val):
        self.heap.append(val)
        self.n+=1
        #print(self.heap)
        bubble=self.n-1
        while not self._is_heap(self._parent(bubble)):
            self.heap[bubble],self.heap[self._parent(bubble)]=self.heap[self._parent(bubble)],self.heap[bubble]
            bubble=self._parent(bubble)
    
    def extrac_min(self):
        
        self.heap[self.n-1],self.heap[0]=self.heap[0],self.heap[self.n-1]
        ans=self.heap.pop(-1)
        self.n-=1
        bubble = 0
        while not self._is_heap(bubble):
            children=self._children(bubble)
            #print('ex',self.n,self.heap,children)
            if (children[1]<self.n and children[0]>=0 and self.heap[children[0]]<=self.heap[children[1]]):
                self.heap[bubble],self.heap[children[0]]=self.heap[children[0]],self.heap[bubble]
                bubble=children[0]
            elif children[1]<self.n:
                self.heap[bubble],self.heap[children[1]]=self.heap[children[1]],self.heap[bubble]
                bubble=children[1]
            else:
                self.heap[bubble],self.heap[children[0]]=self.heap[children[0]],self.heap[bubble]
                bubble=children[0]
            #print(self.heap)
        return ans

    def _is_heap(self,parent):
        '''
        parent index
        '''
        children=self._children(parent)
        ans=True
        #print('chl',parent,children,self.n,ans,self.heap)
        if (children[0]<self.n and children[0]>=0 and self.heap[parent]>self.heap[children[0]]):
            ans = False 
        if (children[1]<self.n and children[1]>=0 and self.heap[parent]>self.heap[children[1]]):
            ans = False
        #print('chl',parent,children,self.n,ans)
        return ans

    def _parent(self,i):
        return max(int((i+1)/2)-1,0)
    
    def _children(self,i):
        i=i+1
        return [2*i-1,2*i+1-1]
    

heap_min=Heap_()
heap_max=Heap_()
median_sum=0

with open("median.txt",'r') as f:
    for row in f:
        
        row=row.rstrip().lstrip()
        if row.isdecimal() and heap_min.n>0 and not int(row)>heap_min.heap[0]:
            heap_max.add_node(-int(row))
            
        elif row.isdecimal(): 
            heap_min.add_node(int(row))
        
        if heap_max.n - heap_min.n >=2 :
            temp=heap_max.extrac_min()
            heap_min.add_node(-temp)
        elif heap_min.n - heap_max.n >=2:
            temp=heap_min.extrac_min()
            heap_max.add_node(-temp)
        
        if (heap_max.n+heap_min.n)%2 == 0:
            median=(-heap_max.heap[0])
        else:
            if heap_min.n>heap_max.n:
                median=heap_min.heap[0]
            else:
                median=-heap_max.heap[0]
        if row.isdecimal():
            median_sum+=median

#print(heap_max.heap)
#print(heap_min.heap)
print('m',median,median_sum,median_sum%10000)
        
        






