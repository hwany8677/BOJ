t=int(input())
point=[0,0,0,0,0] # Q1 Q2 Q3 Q4 AXIS
for i in range(0,t):
    x,y=map(int,input().split())
    if x>0 and y>0: point[0]+=1
    if x<0 and y>0: point[1]+=1
    if x<0 and y<0: point[2]+=1
    if x>0 and y<0: point[3]+=1
    if x==0 or y==0: point[4]+=1
for i in range(0,4): print(f"Q{i+1}: {point[i]}")
print(f"AXIS: {point[4]}")