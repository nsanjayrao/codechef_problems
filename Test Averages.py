# cook your dish here
from itertools import combinations
for i in range(int(input())):
    a,b,c=map(int,input().split())
    comb = combinations([a,b,c],2)
    flag=True
    for i in comb:
        if sum(i)/2 < 35:
            flag = False
    
    if flag == True:
        print('PASS')
    else:
        print('FAIL')
