#Mayor: 4, Treasurer: 2, Chief programmer: 3, Dog-catcher: 5
#lcm=60
#X와 Y의 범위는 어따팔아먹???
start_yr=int(input())
end_yr=int(input())
print(f"All positions change in year {start_yr}")
increment=60
while(start_yr+increment<=end_yr): 
    print(f"All positions change in year {start_yr+increment}")
    increment+=60