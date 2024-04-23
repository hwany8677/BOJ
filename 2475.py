r=input().split()
for i in range(0,len(r)): r[i]=int(r[i])*int(r[i])
s=sum(r)
print(s%10)