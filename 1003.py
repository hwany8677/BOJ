#a: a0
#b: a1
def shuffleFibo(n):
    a,b=0,1
    for _ in range(0,n-1):
        a,b=b,a+b
    print(a,b)
for _ in range(int(input())):
    n=int(input())
    if n==0: 
        print("1 0")
        continue
    elif n==1:
        print("0 1")
        continue
    shuffleFibo(n)