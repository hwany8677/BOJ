input=open(0).readline
for _ in range(int(input())):
    x,y=map(int,input().split())
    if y==x-2 or y==x: print(x+y if (x%2==0 and y%2==0) else x+y-1)
    else: print("No Number")