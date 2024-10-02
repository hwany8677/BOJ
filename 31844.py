s=input()
robot,box,dest=0,0,0
for i in range(10):
    if s[i]=="@": robot=i
    elif s[i]=="#": box=i
    elif s[i]=="!": dest=i
if robot<box and box<dest: print(abs(robot-box)-1+abs(box-dest)-1+1)
elif dest<box and box<robot: print(abs(robot-box)-1+abs(box-dest)-1+1)
else: print(-1)
