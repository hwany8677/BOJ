n,k=map(int,input().split())
count=0
str_k=str(k)
for h in range(0,n+1):
    str_h=str(h).zfill(2)
    for m in range(0,60):
        str_m=str(m).zfill(2)
        for s in range(0,60):
            str_s=str(s).zfill(2)
            if (str_k in str_h) or (str_k in str_m) or (str_k in str_s): count+=1
print(count)