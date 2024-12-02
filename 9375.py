#기어를 하나만 착용할 수 있음 = n
#두가지 -> 
input=open(0).readline
for _ in range(int(input())):
    n=int(input())
    category=dict()
    name,cat=input().rstrip().split()
    if cat not in category: category[cat]=1
    else: category[cat]+=1
    
