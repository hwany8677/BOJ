### 우선순위 ###
#1. 'dongho'가 집에 있는경우 범인 확정, 밑에있는거 싹다무시
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

flagged=[0,0,0] #bumin, cake, lawyer
input() #shii's cake is missing!
n=int(input())
house={0}
house.remove(0)
its_dongho=False
for _ in range(n):
    s=input().rstrip()
    if s=="dongho": its_dongho=True
    if s=="bumin": flagged[0]=1
    if s=="cake": flagged[1]=1
    if s=="lawyer": flagged[2]=1
    house.add(s)
m=int(input())
# witness=[]
for _ in range(m):
    s=input().rstrip()
    temp=len(house)
    house.add(s)
    #집에 있고 목격담이 있거나, 집에 없지만 목격담은 있거나
    if len(house)>temp or len(house)==temp: house.remove(s)
    if s=="bumin": flagged[0]=0
    if s=="cake": flagged[1]=0
    if s=="lawyer": flagged[2]=0
house=sorted(list(house))
if its_dongho: print("dongho") #1번 조건 우선
elif len(house)==1: print(house[0]) #2번 조건 우선
elif flagged[0]: print("bumin") #3번 조건 우선
elif flagged[1]: print("cake") #4번 조건 우선
elif flagged[2]: print("lawyer") #5번 조건 우선
else: 
    try: print(house[0])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    except IndexError: print("swi") #<---- 이새끼 꼭 죽인다 왜 RE쳐나나했네 개씨발 남탓이나 쳐하네