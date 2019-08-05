
'''The goal of this problem is to implement a variant of the 2-SUM algorithm (covered in the Week 6 lecture on hash table applications).

The data.txt file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the ith row of the file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that there are distinct numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.'''

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_1_pas(self):
        alpha=sum2()
        self.assertEqual(427,alpha,alpha)
def sum2():
    hash_t=set()
    with open("sum2.txt") as f:
        for row in f:
            hash_t.add(int(row))
    ans=0
    for t in range(-10000,10001):
        for i in hash_t:
            if not i-t == i and i-t in hash_t:
                ans+=1
                break

    return ans
def sum_(l,r,h):
    return h[l]+h[r]
def sum3():
    hash_t=[]
    with open("sum2.txt") as f:
        for row in f:
            hash_t.append(int(row))
    ans=0
    hash_t.sort()
    left=0
    right=len(hash_t)-1
    max_=10000
    min_=-10000
    counter=set()
    while left<right:
        if sum_(left,right,hash_t) > max_:
            right-=1
        elif sum_(left,right,hash_t) < min_:
            left+=1
        else:
            
            r_n=right
            while sum_(left,r_n,hash_t)>=min_ and sum_(left,r_n,hash_t)<=max_:
                #print(left,r_n)
                counter.add(sum_(left,r_n,hash_t))
                r_n-=1
            l_n=left
            while sum_(l_n,right,hash_t)<=max_ and sum_(l_n,right,hash_t)>=min_:
                #print(l_n,right)
                counter.add(sum_(l_n,right,hash_t))
                l_n+=1
            left+=1
            right-=1
            
    return len(counter)

if __name__=="__main__":
    
    unittest.main()