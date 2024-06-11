n=int(input())
weight,height=[],[]
for _ in range(n): 
    x,y=map(int,input().split())
    weight.append(x)
    height.append(y)
rank=1
biggest=height.index(max(height))
info=[]
for i in range(n): info.append((weight[i],height[i]))
index=[i for i in range(n)]
info.sort(key = lambda x: x[1]) #람다!
