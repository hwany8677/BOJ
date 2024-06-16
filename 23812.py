#for문 지옥
n=int(input())
shelf=[['@'*(n)+' '*(3*n)+'@'*(n)] for _ in range(n)]
connector=[['@'*(5*n)] for _ in range(n)]
for _ in range(2):
    for i in range(n): print(*shelf[i],sep='')
    for i in range(n): print(*connector[i],sep='')
for i in range(n): print(*shelf[i],sep='')