#front와 back의 매치 여부 (front 따로, 그 뒤료 back 검증, 예상 O(2n))
import re
input=open(0).readline
n=int(input())
frontback=input().rstrip().split('*')
for _ in range(n):
    buf=input().rstrip()
    p=re.compile(frontback[0]+'.'+frontback[1])
    