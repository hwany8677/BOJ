#2747번 재활용
x,y=1,1
n=int(input())
if n==0: print("0")
else:
    for i in range(0,n-2):
        x,y=y,x+y
    print(y)
