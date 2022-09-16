# cook your dish here
for i in range(int(input())):
    current_volume,final_volume = map(int,input().split())
    if current_volume > final_volume:
        steps=0
        while current_volume != final_volume:
            current_volume-=1
            steps+=1
        print(steps)
    elif current_volume < final_volume:
        steps=0
        while current_volume != final_volume:
            current_volume += 1
            steps+=1
        print(steps)
    elif current_volume == final_volume:
        print(0)
            
    
