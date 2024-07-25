#max(buf)==carlos -> elected
#otherwise -> nope
from sys import stdin
input=stdin.readline
n=int(input())
buf=[]
for _ in range(n): 
    buf.append(int(input()))
if max(buf)==buf[0]: print("S")
else: print("N")
