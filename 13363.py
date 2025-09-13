n1=int(input())
n2=int(input())
res=0
if n1>n2:
    n1-=n2
    n2=0
    res=(360-n1 if n1>180 else -n1)
elif n1<n2:
    n2-=n1
    n1=0
    res=(n2-360 if n2>180 else n2)
else: res=(0)
res=180 if res==-180 else res
print(res)
