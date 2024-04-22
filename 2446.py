n=int(input())
center=False
s=2*n-1
j=0
for i in range(0,2*n):
    if i==n: center=True
    if not(center):
        print(" "*j,end='')
        print("*"*abs(s))
        j+=1
    else:
        j-=1
        if i==n: #이거 추가안하면 '*'가 중복출력됨
            s-=2
            continue
        print(" "*j,end='')
        print("*"*abs(s))
    s-=2