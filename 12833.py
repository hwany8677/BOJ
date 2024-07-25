a,b,c=map(int,input().split())
res=a^b
to_print=c%2
print(res if to_print==1 else a)
