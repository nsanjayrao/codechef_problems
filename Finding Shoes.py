# cook your dish here
for i in range(int(input())):
    no_of_frnds,no_of_left_shoes=map(int,input().split())
    if no_of_frnds > no_of_left_shoes:
        extra_left_shoes_reqd = no_of_frnds - no_of_left_shoes
        no_of_right_shoes = no_of_frnds
        total_extra_shoes_reqd = extra_left_shoes_reqd + no_of_right_shoes
    elif no_of_frnds < no_of_left_shoes:
        extra_left_shoes_reqd = 0
        no_of_right_shoes = no_of_frnds
        total_extra_shoes_reqd = extra_left_shoes_reqd + no_of_right_shoes
    elif no_of_frnds == no_of_left_shoes:
        total_extra_shoes_reqd = no_of_frnds
    print(total_extra_shoes_reqd)
        
