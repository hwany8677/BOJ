#부산의 자랑! 동래의 희망!
n=int(input())
if n==0:
    print("divide by zero")
    exit(0)
rec=list(map(int,input().split()))
try:
    avg=sum(rec)/n
    ex=0
    for num in rec:
        ex+=num*(1/n)
    res=avg/ex
    print("{:.2f}".format(res))
except ZeroDivisionError:
    print("divide by zero")