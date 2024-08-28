from math import ceil
r,c,n=map(int,input().split())
res=ceil(c/n)*ceil(r/n)
print(res)