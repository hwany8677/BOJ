input=open(0).readline
p,s=map(int,input().split())
status=['Par.','Bogey.','Double Bogey.','Double Eagle.','Eagle.','Birdie.']
hole=1
while(p>0):
    print(f"Hole #{hole}")
    if s==1: print("Hole-in-one.")
    else:
        res=s-p
        if res>2: res=2
        print(status[res])
    print()
    p,s=map(int,input().split())
    hole+=1
