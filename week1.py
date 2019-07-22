def karatsuba(x,y):
    #print(x,'-',y)
    nx=x
    ny=y
    
    if len(nx)<=1 or len(ny)<=1:
        return int(x)*int(y)
    
    a=nx[:int(len(nx)/2)]
    c=ny[:int(len(ny)/2)]

    b=nx[int(len(nx)/2):]
    d=ny[int(len(ny)/2):]

    ac=karatsuba(a,c) 
    bd=karatsuba(b,d)
    ad=karatsuba(a,d)
    bc=karatsuba(b,c)
    #ab_cd=karatsuba(str(int(a)+int(b)),str(int(c)+int(d))) 
    #print(ac,bd,ad,bc,'--')
    

    return 10**(len(nx))*ac+10**(len(nx)/2)*(ad+bc)+bd 

def karatsuba2(x,y):
    x=str(x)
    y=str(y)
    if len(x)%2 > 0:
        x='0'+x 
    if len(y)%2 > 0:
        y='0'+y 
    
    

    return karatsuba(x,y)
n1=3141592653589793238462643383279502884197169399375105820974944592
n2=2718281828459045235360287471352662497757247093699959574966967627

n1,n2=100,20

print(karatsuba2(n1,n2),'/n',n1*n2)

