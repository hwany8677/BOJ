#15% 절사평균 -> (n*15)/100 를 반올림한걸 위아래로 빼줌
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
#    print(f"{sc}, len={len(sc)}, trim={trim}")
    s=0
    for i in range(trim,len(sc)-trim):
        s+=sc[i]
#    print(f"sum={s}")
    print(n_round(s/(len(sc)-trim*2)))