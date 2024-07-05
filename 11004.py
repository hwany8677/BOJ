#개날먹코드 - 이렇게 풀면 절대안됨
n,k=map(int,input().split())
buf=list(map(int,input().split()))
buf.sort()
print(buf[k-1])