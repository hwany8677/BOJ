#ㅋㅋ
from sys import stdin
buf=[]
for _ in range(int(input())): buf.append(int(stdin.readline()))
buf.sort() #<---- 이거 의외로빠름 찾아보니 O(n*log n)이라고??????
print(*buf,sep='\n')