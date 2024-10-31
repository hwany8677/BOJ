#'일단' PyPy로 돌아가긴 함
n=int(input())
buf=list(map(int,input().split()))
desired=list(map(int,input().split()))
for i in range(n-1,0,-1):
    if buf==desired: 
        print(1)
        exit(0)
    mx_idx=buf.index(max(buf[:i+1]))
    if mx_idx!=i: buf[i],buf[mx_idx]=buf[mx_idx],buf[i]
print(0)
