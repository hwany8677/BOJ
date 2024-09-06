#정석대로 안푼것
n=int(input())
nums=dict()
buf=list(map(int,input().split()))
for soot_ja in buf:
    try: nums[soot_ja]+=1
    except KeyError: nums[soot_ja]=1
n=int(input())
buf=list(map(int,input().split()))
for soot_ja in buf:
    try: print(nums[soot_ja],end=' ')
    except KeyError: print(0,end=' ')
print()