#(floor, parent info, itself) <-- Tuple format 
input=open(0).readline
n,k=map(int,input().split())
floor_length=[1] #배열에 접근할 시 
while(n!=0 or k!=0):
    buf=list(map(int,input().split()))
    tree=[(0,None,buf[0])]
    floor=1
    parent=buf[0]
    prev=buf[1]-1
    to_clear=0
    #1. Check if the list is consecutive
    #If not, 
    for i in range(1,n):
        itself=buf[i]
        tree.append((floor,parent,itself))
        to_clear+=1