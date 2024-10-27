#Directions
#    S
#  Z   I
#    J
agent_pos=list(map(int,input().split()))
k=int(input())
instructions=input()
x,y=0,0
res=[]
for i in range(k+1):
    can_hear=[
            [x-1,y+1],[x,y+1],[x+1,y+1],
            [x-1,y],[x,y],[x+1,y],
            [x-1,y-1],[x,y-1],[x+1,y-1]
    ]
    for eaves in can_hear:
        if eaves==agent_pos: 
            res.append(i)
            break
    if i>k-1: break
    #Pos update
    inst=instructions[i]
    if inst=='S': y+=1
    elif inst=='J': y-=1
    elif inst=='Z': x-=1
    elif inst=='I': x+=1
if len(res)==0: print(-1)
else:
    for element in res: print(element)
