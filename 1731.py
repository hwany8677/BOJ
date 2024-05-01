#입력: 자연수로 제한됨
#즉, 귀납적인 방법만 보면 끝
n=int(input())
a=[]
for i in range(0,n): a.append(int(input()))
if a[1]-a[0]==a[2]-a[1]: print(a[n-1]+(a[1]-a[0]))
else: print(a[n-1]*(int(a[1]/a[0])))
