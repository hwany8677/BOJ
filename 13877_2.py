#int(buf,8),int(buf,16)
input=open(0).readline
p=int(input())
for _ in range(p): 
    k,buf=input().rstrip().split()
    oct_res=int(buf,8) if max(buf)<'8' else 0
    print(f"{k} {oct_res} {buf} {int(buf,16)}")
