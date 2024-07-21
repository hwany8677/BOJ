#Naive approach, O(n²)
from sys import stdin
input=stdin.readline
def Sn(lisT):
    res=[lisT[0]]
    for i in range(1,len(lisT)):
        res.append(lisT[i]+res[i-1])
    return res
n,m=map(int,input().split())
buf=list(map(int,input().split()))
count=0
S=Sn(buf) #구간합 base
#4 2
#1 1 1 1
#try: 
#S1, S2, S3, S4
#S3-S1, S4-S2 (2 elements)
#S4-S1 (3 elements)
#
#10 5
#1 2 3 4 2 5 3 1 1 2
#try:
#S1, S2, ..., S10 (full seek)
#S3-S1, S4-S2, ..., S10-S8 (2 elements)
#S4-S1, S5-S2, ..., S10-S7 (3 elements)
#...
#S9-S1, S10-S2 (8 elements)
#S10-S1 (9 elements)
#-> end가 len(S) 넘어가면 각각 while문 끝내는걸로
#새로운 end는 i+1로 (i=0 시작, end=1(제외),2,3,...)
count=0
length=len(S)
for i in range(0,n):
    start,end=0,i+1
    if i==0: #S1, S2, ..., S10 + a1, a2, ..., a10 (full seek) 
        for j in range(0,n): 
            if buf[j]==m: count+=1
            elif S[j]==m: count+=1
        continue
    while(end<length): 
        if S[end]-S[start]==m: count+=1 #S3-S1, S4-S2, ..., S10-S8 
        end+=1
        start+=1
print(count)