#숫자를 가지고 놀아야함
from sys import stdin
input=stdin.readline

n=int(input())
buf=[]
for _ in range(n): buf.append(int(input()))
if sorted(buf)==buf:
    print(1)
    exit(0)
buf_sorted=sorted(buf)
idx=[i for i in range(n)]
temp=zip(buf,idx)
idx_before=[i for _,i in sorted(temp)]
index_cha=[idx[i]-idx_before[i] for i in range(n)]
mn=min(index_cha)
print(abs(mn)+1)