#B >> S >> G >> P >> D
n=int(input())
diff=input().split()
diff2=[]
for i in range(len(diff)):
    if diff[i][0]=='B': diff2.append(0+1000-int(diff[i][1:]))
    if diff[i][0]=='S': diff2.append(10000+1000-int(diff[i][1:]))
    if diff[i][0]=='G': diff2.append(20000+1000-int(diff[i][1:]))
    if diff[i][0]=='P': diff2.append(30000+1000-int(diff[i][1:]))
    if diff[i][0]=='D': diff2.append(40000+1000-int(diff[i][1:]))
diff3=list(diff2)
diff3.sort()
diff4=[]
for i in range(len(diff2)):
    if diff2[i]!=diff3[i]: diff4.append(i)
if len(diff4): 
    print("KO")
    print(f"{diff[diff4[1]]} {diff[diff4[0]]}")
else: print("OK")