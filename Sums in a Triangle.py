# cook your dish here
for i in range(int(input())):
    n=int(input())
    arr=[]
    for i in range(n):
        col= list(map(int,input().split()))
        arr.append(col)
    #print(arr)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if arr[i][j] > arr[i][j+1]:
                arr[i-1][j] = arr[i-1][j] + arr[i][j]
            else:
                arr[i-1][j] = arr[i-1][j] + arr[i][j+1]
    print(arr[0][0])
