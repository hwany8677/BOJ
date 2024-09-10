#시이야... 망고빙수나 먹어...
#
#
### 우선순위 ###
#1. 'dongho'가 집에 있는경우 범인 확정
#2. 집에 있던 사람 중 목격담리스트에 안 오른 사람이 단 한 명이면, 그사람은 범인
#3. 목격담리스트에 안 오른 상태고 이름이 'bumin'이고 집에 있다면, 범인 확정
#4. 목격담리스트에 안 오른 사람의 이름이 'cake'이고 집에 있으면 범인 확정
#5. 목격담리스트에 안 오른 사람의 이름이 'lawyer'이고 집에 있으면 범인 확정
#6. 시이가아닌 사람들중 목격담리스트에 안 오르고 이름이 사전순으로 제일빠른 사람이 이 범인
#
#bumin, cake, lawyer는 목격담을 가지는순간 탈락임
#dongho > bumin > cake > lawyer
from sys import stdin
input=stdin.readline

flagged={ #0: Not found, 1: Found
    "bumin":0,
    "cake":0,
    "lawyer":0
}
n=int(input())
house=[]
criminal=''
for _ in range(n):
    s=input()
    if s=="dongho":
        print(s)
        exit(0)
    if s=="bumin" or s=="cake" or s=="lawyer":
        flagged[s]=1
    flagged[s]=1
    house.append(s)
m=int(input())
witness=[]
for _ in range(m):
    s=input()
    if s=="bumin": flagged[s]=0
    if s=="cake": flagged[s]=0
    if s=="lawyer": flagged[s]=0
    if s in house: