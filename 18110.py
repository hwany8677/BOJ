#15% 절사평균 -> (n*15)/100 를 반올림한걸 위아래로 빼줌
#정렬 쓰지 않고 빈도 수를 탐색하여 위아래 때버리기
#이거 왜 시간초과뜸?? PyPy3를 안 쓰면 죽나요?
#from time import process_time as p
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
    diff=[0 for _ in range(31)]
    for _ in range(0,n): 
        buf=int(input())
        diff[buf]+=1
        sc.append(buf)
#    t0=p()
    trim=n_round((n*15)/100)
    s=0
    start,end=0,0
    idxSum=0
    i=1
    #여기서 반복문 우겨넣어서 복잡하게 만들긴 싫음
    #좀 그만 붙들고 싶다 ㅅㅂ
    real_len=0
    while(1):
        if (idxSum+diff[i]>trim):
            s+=i*(idxSum+diff[i]-trim)
            real_len+=idxSum+diff[i]-trim
            start=i
            break
        else:
            idxSum+=diff[i]
            i+=1
    idxSum=0
    i=30
    while(1):
        if (idxSum+diff[i]>trim):
            s+=i*(idxSum+diff[i]-trim)
            real_len+=idxSum+diff[i]-trim
            end=i
            break
        else:
            idxSum+=diff[i]
            i-=1
    for i in range(start+1,end): 
        s+=i*diff[i]
        real_len+=diff[i]
    print(n_round(s/real_len))
#    t=p()
#    print(f"Time took to process: {t-t0} seconds")