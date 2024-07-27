#뚊, 쀼장, 쁐 X
n,m=map(int,input().split())
isEyfa=0
s=[]
s2=[]
for _ in range(n): s.append(input())
for _ in range(n): s2.append(input())
for i in range(n):
    temp=[]
    for char in s[i]:
        temp.append(char)
        temp.append(char)
    temp=''.join(temp)
    if temp==s2[i]: isEyfa+=1
print("Eyfa" if isEyfa==n else "Not Eyfa")