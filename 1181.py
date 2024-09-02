#1. Shortest first
#2. In alphabetical order
from sys import stdin
input=stdin.readline
buf=[]
n=int(input().strip('\n'))
mx_len=0
for _ in range(n):
    s=input().strip('\n')
    if len(s)>mx_len: mx_len=len(s)
    buf.append(s)
lenbylen=[[] for _ in range(mx_len)]
for i in range(mx_len):
    for j in range(n):
        s_len=len(buf[j])
        if s_len==i+1: lenbylen[i].append(buf[j])
for i in range(mx_len):
    lenbylen[i]=sorted(set(lenbylen[i]))
    lenbylen[i].sort()
for i in range(mx_len):
    for j in range(len(lenbylen[i])):
        print(lenbylen[i][j])