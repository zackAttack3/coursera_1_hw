a=[[0]*10]
for i in range(1,10):
    a.append(list([i]*10))
    for j in range(10):
        a[i][j]=a[i-1][j]+j