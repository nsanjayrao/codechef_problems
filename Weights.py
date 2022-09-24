# cook your dish here
from itertools import combinations
for i in range(int(input())):
    w,x,y,z=map(int,input().split())
    comb_1=combinations([x,y,z],1)
    comb_2=combinations([x,y,z],2)
    comb_3=combinations([x,y,z],3)
    comb=[]
    #flag=False
    for i in comb_1:comb.append(i)
    for i in comb_2:comb.append(i)
    for i in comb_3:comb.append(i)
    count=0
    for i in comb:
        if sum(i)==w:
            count+=1
            
    if count>=1:
        
        print('YES')
    else:
        print('NO')
    
