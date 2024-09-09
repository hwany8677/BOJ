#Naive method
#ㅅㅂ 이게 왜되지??? 왜 5초준거지?
from sys import stdin
input=stdin.readline

passwd={}
n,m=map(int,input().split())
for _ in range(n):
    s=input().rstrip().split()
    passwd[s[0]]=s[1]
for _ in range(m):
    print(passwd[input().rstrip()])
