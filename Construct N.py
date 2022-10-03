# cook your dish here
for i in range(int(input())):
    n=int(input())
    x=0
    c=0
    while(x*2<=n):
        if (n-2*x)%7==0:
            c+=1
            print('YES')
            break
        x+=1
    if c==0:
        print('NO')
    
