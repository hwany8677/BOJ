#3구: 2개
#4구: 2개
#5구: 3개
#6구: 3개
#7구: 4개
#8구: 4개
n,k=map(int,input().split())
a=list(map(int,input().split()))
port=[0,0,0,2,2,3,3,4,4]
for element in a: n-=port[element]
if n<=0: print("YES")
else: print("NO")