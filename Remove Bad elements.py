# cook your dish here
from statistics import mode
for i in range(int(input())):
    n=int(input())
    arr = list(map(int,input().split()))
    num = mode(arr)
    count=0
    for i in arr:
        if i != num:
            count+=1
    print(count)
