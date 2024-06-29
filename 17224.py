#쉬움 only 100점 어려움 140점
n,l,k=map(int,input().split())
sub1,sub2=[],[]
for _ in range(n): 
    s1,s2=map(int,input().split())
    sub1.append(s1)
    sub2.append(s2)
s=0
for i in range(len(sub2)):
    if sub2[i]<=l and k!=0: 
        s+=140
        sub1[i]=l+1
        k-=1
for i in range(len(sub1)):
    if sub1[i]<=l and k!=0:
        s+=100
        k-=1
print(s)