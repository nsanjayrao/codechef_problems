# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    multiply=a*b
    while(b):
        a,b=b,a%b
    hcf=a
    lcm=multiply/hcf
    print(hcf,int(lcm))
