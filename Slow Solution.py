# cook your dish here
for i in range(int(input())):
    maxT,maxN,sumN=map(int,input().split())
    temp=0
    maxi=0
    for t in range(maxT):
        temp=temp+maxN
        if temp<=sumN:
            maxi=maxi + maxN**2
        else:
            maxi=maxi+(maxN-(temp-sumN))**2
            break
    print(maxi)
