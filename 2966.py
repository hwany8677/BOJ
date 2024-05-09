#길이 n만큼 append?
n=int(input())
ans=input()
ad=["A","B","C"]
br=["B","A","B","C"]
go=["C","C","A","A","B","B"]
c=[0,0,0]
for i in range(0,n):
	if ans[i]==ad[i%3]: c[0]+=1
	if ans[i]==br[i%4]: c[1]+=1
	if ans[i]==go[i%6]: c[2]+=1
#에라몰라 걍 for문 2번돌려~
max=0
maxC=[0,0,0]
for i in range(0,3):
	if c[i]>=max: 
		max=c[i]
for i in range(0,3):
	if c[i]==max:
		maxC[i]+=1
print(max)
if maxC[0]: print("Adrian")
if maxC[1]: print("Bruno")
if maxC[2]: print("Goran")
