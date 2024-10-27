#This somehow took me 5 minutes to read...
#I'm dyslexic lmao
input=open(0).readline
base=[i for i in range(1000)]
s1=[base[0]]
for i in range(1,1000): s1.append(base[i]+s1[i-1])
s2=[s1[0]]
for i in range(1,1000): s2.append(s1[i]+s2[i-1])
for i in range(1,int(input())+1):
    n=int(input())
    print(f"{i}: {n} {s2[n]}")
