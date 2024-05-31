#Minimum requirement: L
#VIP requirement: K (sum of 3 members' rating)
#CPython에선 안되는데 PyPy에선 되는 이상한코드
#도대체 뭐가 문제길래 실행시간이 길게나오는겨??? 설마 for문으로 받는거때문에??
n,k,l=map(int,input().split())
qualified=0
rating=[]
for i in range(0,n):
  x1,x2,x3=map(int,input().split())
  if x1<l or x2<l or x3<l: continue
  sigma=x1+x2+x3
  if sigma>=k:
    qualified+=1
    for r in [x1,x2,x3]: rating.append(r)
print(qualified)
print(*(v for v in rating))