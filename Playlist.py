# cook your dish here
for i in range(int(input())):
    journey_duration,each_song_duration = map(int,input().split())
    a=0
    b=0
    c=0
    duration=0
    flag = True
    while flag:
        
        duration += each_song_duration
        
        if duration > journey_duration:
            flag = False
            break
        a+=1
        
        duration += each_song_duration
        
        if duration > journey_duration:
            flag = False
            break
        b+=1
        duration += each_song_duration
        
        if duration > journey_duration:
            flag = False
            break
        c+=1 
    print(c)    
