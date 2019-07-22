def mergeSort(a,inv):

    if len(a)==1:
        return a
    else:
        n=int(len(a)/2)
        left=mergeSort(a[:n],inv)
        right=mergeSort(a[n:],inv)
    return merge(left,right,inv)

        

def merge(left,right,inv):
    lr=[]
    il,ir,ilr=0,0,0
    print(left,right)
    while left is not None and right is not None and il<len(left) and ir<len(right):
        if left[il]<=right[ir]:
            lr.append(left[il])
            il+=1
        else:
            lr.append(right[ir])
            inv[0]+=len(left)-il
            ir+=1
            
        ilr+=1
    if left is not None and il<len(left):
        lr=lr+left[il:]
    if right is not None and ir<len(right):
        lr=lr+right[ir:]
    print('---',lr,inv)
    return lr

def mergeSort2(a,l,r,inv):
    #print('--,',l,r)
    if l==r:
        return None
    else:
        mid = int(l+r)/2
        mergeSort2(a,l,mid,inv)
        mergeSort2(a,mid+1,r,inv)
        merge2(a,l,r,int(l+r)/2,inv)
        return None

def merge2(a,l,r,mid,inv):
    il,ir=l,mid+1
    #print(a,'')
    while il <= ir and ir <r:
        
        if a[il]<=a[ir]:
            il+=1
        else:
            a[il],a[ir]=a[ir],a[il]
            inv[0]+=ir-il
            ir= min(ir+1,ir)
        #print(a,'*',inv)
    
    if a[mid]>a[mid+1]:
        a[mid],a[mid+1]=a[mid+1],a[mid]
        inv[0]-=1
    #print(a,' ',l,r,mid,inv,il,ir)
    return None
inv=[0]
a=[1,5,3,2,4]
mergeSort(a,inv)
print(a,inv)

with open('week2.txt', 'r') as f:
    x = f.readlines()
inv=[0]
mergeSort2([int(xi) for xi in x],0,len(x)-1,inv)
print(inv)

