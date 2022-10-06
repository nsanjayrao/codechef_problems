# cook your dish here
for i in range(int(input())):
    n=int(input())
    arr_c=list(map(int,input().split()))
    a=arr_c[0]
    k=0
    for i in range(n):
        if arr_c[i] > a:
            k+=i
            break
    if k > 0:
        a=arr_c[:k]
        b=arr_c[k:]
        print(len(a))
        print(*a)
        print(len(b))
        print(*b)
    else:
        print(-1)
