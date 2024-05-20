n=int(input())
s=[]
for _ in range(0,n): s.append(input())
for _ in range(1,n+1): print(f"{_}. {s[_-1]}")