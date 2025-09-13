input=open(0).readline
n=int(input())
yester=input().rstrip()
today=input().rstrip()
count=0
for i in range(n):
    if yester[i]=='C' and today[i]=='C': count+=1
print(count)
