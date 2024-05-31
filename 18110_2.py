#이것도 PyPy3로 안돌리면 시간초과나옴 ㅅㅂ
from sys import setrecursionlimit as rec
import math
def qSort(lisT):
    if len(lisT)<2: return lisT
    if len(lisT)==2:
        if lisT[0]==lisT[1]: return lisT
        elif lisT[0]>lisT[1]: return [lisT[1],lisT[0]]
        elif lisT[0]<lisT[1]: return [lisT[0],lisT[1]]
    pivot=lisT[n_round((len(lisT)-1)/2)] 
    ls,bg=[],[]
    for i in range(0,len(lisT)):
        if lisT[i]<=pivot and i!=len(lisT)-1: ls.append(lisT[i])
        elif lisT[i]>pivot: bg.append(lisT[i])
    lesserThan=qSort(ls)
    biggerThan=qSort(bg)
    return lesserThan+[pivot]+biggerThan
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
    rec(99999999)
    sc=qSort(sc)
    trim=n_round((n*15)/100)
    s=0
    for i in range(trim,len(sc)-trim):
        s+=sc[i]
    print(n_round(s/(len(sc)-trim*2)))