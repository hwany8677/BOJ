#Median of Three
from time import process_time as p
from sys import stdin
def medOf3(left,right):
    if left>=right: return [right,left]
    if left<right: return [left,right]
def qSort(lisT):
    lisT[0],lisT[len(lisT)-1]=map(int, medOf3(lisT[0],lisT[len(lisT)-1]))
    if len(lisT)<2: return lisT
    if len(lisT)==2:
        if lisT[0]==lisT[1]: return lisT
        elif lisT[0]>lisT[1]: return [lisT[1],lisT[0]]
        elif lisT[0]<lisT[1]: return [lisT[0],lisT[1]]
    pivot=lisT[len(lisT)//2]
    ls,bg=[],[]
    for i in range(0,len(lisT)):
        if lisT[i]<=pivot and i!=len(lisT)-1: ls.append(lisT[i])
        elif lisT[i]>pivot: bg.append(lisT[i])
    lesserThan=qSort(ls)
    biggerThan=qSort(bg)
    return lesserThan+[pivot]+biggerThan
buf=[]
for _ in range(int(input())): buf.append(int(stdin.readline()))
t0=p()
# res=qSort(buf)
buf.sort()
t=p()
print(*buf,sep='\n')
print(f"Time took to process: {t-t0} seconds")