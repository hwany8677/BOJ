#진짜 이 문제는 전설이다...
import math
def n_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)
n=int(input())
if n==0:
    print(0)
else:
    sc=[]
    for _ in range(0,n): sc.append(int(input()))
    sc.sort()
    trim=n_round((n*15)/100)
    for _ in range(0,trim):
        sc.remove(sc[0])
        sc.remove(sc[len(sc)-1])
    print(n_round(sum(sc)/len(sc)))

    